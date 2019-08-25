from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.template.defaultfilters import truncatewords
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import CommentForm, PostForm
from .models import Ad_Post, Ad_Comment
from .forms import Ad_Comment

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
    return render(request, 'ad_post/ad_post_form.html', {
        'form': form,
    })

class PostListView(ListView):
    template_name = "ad_post/ad_post_list2.html"
    model = Ad_Post

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Ad_Post

    def render_to_response(self, context):
        if self.request.is_ajax():
            return JsonResponse({
                'title':self.object.title,
                'summary':truncatewords(self.object.content, 100),
            })
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

post_detail = PostDetailView.as_view()

class PostUpdate(UpdateView):
    model = Ad_Post
    fields = ['title', 'content', 'photo']

post_edit = PostUpdate.as_view()

def comment_new(request, post_pk):
    post = Ad_Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 자동으로 save 시키지 않는다.
            comment.author_id = request.user.id
            comment.post_id = post.pk
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('ad_post:post_detail', post_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'ad_post/ad_post_form.html', {
        'form': form,
    })


@login_required
def comment_edit(request, post_pk, pk):
    comment = Ad_Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Ad_Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('/ad_post/{}'.format(post_pk))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'ad_post/post_form.html', {
        'form':form,
    })

def post_remove(request, pk):
    post = get_object_or_404(Ad_Post, pk=pk)
    post.delete()
    messages.success(request, '게시글을 삭제했습니다.')
    return redirect('ad_post:post_list')


class CommentUpdateView(UpdateView):
    model = Ad_Comment
    form_class = CommentForm

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_edit = CommentUpdateView.as_view()

def test1(request):
    return render(request, 'ad_post/ad_post_list2.html')