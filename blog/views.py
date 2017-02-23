from django.shortcuts import render
from django.views import generic

from django.urls import reverse
from .models import Post





# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.all().order_by('-id')


class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

