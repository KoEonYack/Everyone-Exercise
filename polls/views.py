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
    form_class = PostSearchForm
    template_name = 'polls/search.html'

    def form_valid(self, form):
        search_word = self.request.POST['search_word']
        post_list = Info.objects.filter(Q(name__icontains=search_word) | Q(address__icontains=search_word))

        context = {}
        context['form'] = form
        context['search_term'] = search_word
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

def maps(request, maps_id):
    template_name = 'polls/maps.html'
    information = get_object_or_404(Info, pk=maps_id)

    return render(request, template_name,
                  context={'comment_form': CommentForm(), 'information': information})

def comment_new(request, map_pk):
    info = Info.objects.get(pk=map_pk)
    rate_count = 0
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author_id = request.user.id
            comment.info_id = info.pk
            comment.rate = request.POST['rate']
            for rate in comment.rate:
                if rate == '★':
                    rate_count += 1
            info.rate_sum += rate_count
            info.count += 1
            info.rate_ave = round(info.rate_sum/info.count,1)
            info.save()
            comment.save()
            messages.success(request, '메시지를 작성하였습니다.')
            return redirect('polls:maps', map_pk)  # post.get_absolute_url() => post detail
    else:
        form = CommentForm()
    return render(request, 'poll/maps.html', {
        'form': form })
