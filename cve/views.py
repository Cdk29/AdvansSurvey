from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import CVE


class IndexView(generic.ListView):
    template_name = 'cve/index.html'
    context_object_name = 'latest_cve_list'

    def get_queryset(self):
        return CVE.objects.order_by('-pub_date')


class ArchivesView(generic.ListView):
    template_name = 'cve/archives.html'
    context_object_name = 'latest_cve_list'

    def get_queryset(self):
        return CVE.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = CVE
    template_name = 'cve/detail.html'
