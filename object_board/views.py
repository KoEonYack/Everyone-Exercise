import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaultfilters import truncatewords
from .forms import FoodSearchForm
from django.db.models import Q
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Food, METs, ObPost, ObjComment
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import CommentForm, PostForm

@permission_required('admin.can_add_log_entry')
def csv_upload_food(request):
    template = "object_board/csv_upload_food.html"
    prompt = {
        'food': 'only food csv file'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Food.objects.update_or_create(
            kind = column[0],
            name = column[1],
            standard = column[2],
            kcal = column[3],
        )
    context = {}
    return render(request, template, context)

@permission_required('admin.can_add_log_entry')
def csv_upload_mets(request):
    template = "object_board/csv_upload_mets.html"
    prompt = {
        'mets' : 'only mets csv file'
    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = METs.objects.update_or_create(
            power = column[0],
            name = column[1],
            mets = column[2],
        )
    context = {}
    return render(request, template, context)

class FoodSearchFormView(FormView):
    # form_class를 forms.py에서 정의했던 PostSearchForm으로 정의
    form_class = FoodSearchForm
    template_name = 'object_board/score.html'

    # 제출된 값이 유효성검사를 통과하면 form_valid 메소드 실행
    # 여기선 제출된 search_word가 PostSearchForm에서 정의한대로 Char인지 검사
    def form_valid(self, form):

        # 제출된 값은 POST로 전달됨
        # 사용자가 입력한 검색 단어를 변수에 저장
        search_food = self.request.POST['search_food']
        # Post의 객체중 제목이나 설명이나 내용에 해당 단어가 대소문자관계없이(icontains) 속해있는 객체를 필터링
        # Q객체는 |(or)과 &(and) 두개의 operator와 사용가능
        post_list = Food.objects.filter(Q(name__icontains=search_food))
        exercise_list = METs.objects.all()
        context = {}
        # context에 form객체, 즉 PostSearchForm객체 저장
        context['form'] = form
        context['search_term'] = search_food
        context['object_list'] = post_list
        context['exercise_list'] = exercise_list

        return render(self.request, self.template_name, context)



class PostListView(ListView):
    #template_name = "object_board/obpost_list.html"
    template_name = "object_board/exercise.html"
    model = ObPost

class FoodPostListView(PostListView, FoodSearchFormView):
#class FoodPostListView(FoodSearchFormView):
    pass

new_obpost_list = FoodPostListView.as_view()

obpost_list = PostListView.as_view()


class PostDetailView(DetailView):
    model = ObPost

    def render_to_response(self, context):
        if self.request.is_ajax():
            return JsonResponse({
                'title': self.object.title,
                'summary':truncatewords(self.object.content, 100),
            })
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

post_detail = PostDetailView.as_view()

def post_remove(request, pk):
    post = get_object_or_404(ObPost, pk=pk)
    post.delete()
    messages.success(request, '게시글을 삭제했습니다.')
    return redirect('object_board:exercise')

def comment_new(request, post_pk):
    post = ObPost.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 자동으로 save 시키지 않는다.
            comment.author_id = request.user.id
            comment.post_id = post.pk
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('object_board:post_detail', post_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'object_board/obpost_form.html', {
        'form': form,
    })

class PostUpdate(UpdateView):
    model = ObPost
    fields = ['title', 'content', 'finish']

post_edit = PostUpdate.as_view()


def comment_new(request, post_pk):
    post = ObPost.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 자동으로 save 시키지 않는다.
            comment.author_id = request.user.id
            comment.post_id = post.pk
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('object_board:obpost_detail', post_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'object_board/obpost_list.html', {
        'form': form,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 자동으로 save 시키지 않는다.
            post.author_id = request.user.id
            post.save()
            return redirect(post)  # post.get_absolute_url() => post detail
    else:
        form = PostForm()
    return render(request, 'object_board/obpost_form.html', {
        'form': form,
    })