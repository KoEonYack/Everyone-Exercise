from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.template.defaultfilters import truncatewords
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib import messages
from blog.forms import CommentForm, PostForm
from .models import Post, Comment
from .forms import Comment

'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
       context = super(PostDetailView, self).get_context_data(**kwargs)
       context['commentform'] = CommentForm()
       return context

    def post(self, request, pk):
       post = get_object_or_404(Post, pk=pk)
       form = CommentForm(request.POST)

       if form.is_valid():
           comment = form.save(commit=False)
           comment.post = Post.objects.get(pk=pk)
           comment.author = request.user
           comment.save()
           return redirect('/blog/{}/'.format(pk))

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.author = request.user
            comment.save()
            return redirect('/blog/{}/'.format(pk))
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post':post,
    })
'''

'''
def comment_new(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.object.get(pk=post_pk)
            comment.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
'''

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
    return render(request, template_name='index.html')

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
    #messages.WARNING(request, '메시지를 삭제했습니다.')
    return redirect('blog:post_list')


'''
class PostCreateView(CreateView):
    model = Post
    fields=['title', 'content', 'sport', 'location', 'people', 'duration']

post_new = PostCreateView.as_view()
'''

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


'''
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        print(self.kwargs['post_pk'])
        comment.post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url(self.object.post)

comment_new = CommentCreateView.as_view()
'''

'''
@login_required
def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('/blog/{}'.format(post_pk))
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_form.html', {
        'form':form,
    })
'''

