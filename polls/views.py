import csv, io
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView

from polls.models import Info
from polls.forms import PostSearchForm, CommentForm
from django.db.models import Q
from django.views.generic.edit import FormView
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
import folium
import googlemaps

'''
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message': "You did't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})
# Create your views here.
'''

# @permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template = "polls/csv_upload.html"
    prompt = {
        'order' : 'Order of the CSV should be name, address, post_number, homepage, number, introduce'
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
        _, created = Info.objects.update_or_create(
            name = column[0],
            address = column[1],
            post_number = column[2],
            homepage = column[3],
            number = column[4],
            introduce = column[5],
        )
    context = {}
    return render(request, template, context)


class SearchFormView(FormView):
    # form_class를 forms.py에서 정의했던 PostSearchForm으로 정의
    form_class = PostSearchForm
    template_name = 'polls/search.html'

    # 제출된 값이 유효성검사를 통과하면 form_valid 메소드 실행
    # 여기선 제출된 search_word가 PostSearchForm에서 정의한대로 Char인지 검사
    def form_valid(self, form):

        # 제출된 값은 POST로 전달됨
        # 사용자가 입력한 검색 단어를 변수에 저장
        search_word = self.request.POST['search_word']
        # Post의 객체중 제목이나 설명이나 내용에 해당 단어가 대소문자관계없이(icontains) 속해있는 객체를 필터링
        # Q객체는 |(or)과 &(and) 두개의 operator와 사용가능
        post_list = Info.objects.filter(Q(name__icontains=search_word))

        context = {}
        # context에 form객체, 즉 PostSearchForm객체 저장
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)


def maps(request, maps_id):
    template_name = 'polls/maps.html'
    information = get_object_or_404(Info, pk=maps_id)

    #return render(request, template_name, {'information':information},
    return render(request, template_name,
                  context={'comment_form': CommentForm(), 'information': information})

'''
class MapDetailView(DetailView):
    model = Info
    template_name = 'polls/maps.html'

    def render_to_response(self, context):
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

maps = MapDetailView.as_view( ) 
'''


def comment_new(request, map_pk):
    info = Info.objects.get(pk=map_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 자동으로 save 시키지 않는다.
            comment.author_id = request.user.id
            comment.info_id = info.pk
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('polls:maps', map_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'poll/maps.html', {
        'form': form,
    })
