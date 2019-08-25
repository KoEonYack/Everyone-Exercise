from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.template.defaultfilters import truncatewords
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib import messages
from blog.forms import CommentForm, PostForm
from .models import Post, Comment
from .forms import Comment

def comment_new(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) # 자동으로 save 시키지 않는다.
            comment.author_id = request.user.id
            comment.post_id = post.pk
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('blog:post_detail', post_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def main(request):
    return render(request, template_name='blog/main.html')

class PostDetailView(DetailView):
    model = Post

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

post_list = ListView.as_view(model=Post)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content', 'sport', 'location', 'people', 'duration', 'finish']
post_edit = PostUpdate.as_view()


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_edit = CommentUpdateView.as_view()


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')

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
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

