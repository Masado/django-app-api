from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Annotation


class IndexView(generic.ListView):
    template_name = 'annotation/index.html'
    context_object_name = 'latest_annotation_list'

    def get_queryset(self):
        """
        Return the last five published annotations.
        """
        return Annotation.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Annotation
    template_name = 'annotation/detail.html'
