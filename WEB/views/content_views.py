from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.core import serializers
import json

from django.views import generic

from ..forms import *
from ..models import *
from search_listview.list import SearchableListView


# def news(request):
#     get_program = Programme.objects.all()
#     page = request.GET.get('page', 1)
#
#     paginator = Paginator(get_program, 10)
#     try:
#         program = paginator.page(page)
#     except PageNotAnInteger:
#         program = paginator.page(1)
#     except EmptyPage:
#         program = paginator.page(paginator.num_pages)
#
#     context = {
#         'programme': program,
#     }
#     return render(request, 'WEB/staff/news.html', context)


class NewsList(generic.ListView):
    model = Content
    template_name = "WEB/staff/news.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Content.objects.filter(
                Q(name__icontains=query)
                ,
                Q(type__name="NEWS")
            )
        else:
            return Content.objects.filter(type__name="NEWS")

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


class EventList(generic.ListView):
    model = Content
    template_name = "WEB/staff/event.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Content.objects.filter(
                Q(name__icontains=query)
                ,
                Q(type__name="EVENT")
            )
        else:
            return Content.objects.filter(type__name="EVENT")

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


class DownloadsList(generic.ListView):
    model = Content
    template_name = "WEB/staff/downloads.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Content.objects.filter(
                Q(name__icontains=query)
                ,
                Q(type__name="DOWNLOADS")
            )
        else:
            return Content.objects.filter(type__name="DOWNLOADS")

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


class ReportsList(generic.ListView):
    model = Content
    template_name = "WEB/staff/reports.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Content.objects.filter(
                Q(name__icontains=query)
                ,
                Q(type__name="REPORT")
            )
        else:
            return Content.objects.filter(type__name="REPORT")

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


class NewsLettersList(generic.ListView):
    model = Content
    template_name = "WEB/staff/news_letter.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Content.objects.filter(
                Q(name__icontains=query)
                ,
                Q(type__name="NEWS LETTER")
            )
        else:
            return Content.objects.filter(type__name="NEWS LETTER")

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


class ProgrammeList(generic.ListView):
    model = Content
    template_name = "WEB/staff/programme.html"

    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Programme.objects.filter(
                Q(name__icontains=query)

            )
        else:
            return Programme.objects.all()

    # context_object_name = 'programme'
    # paginate_by = 10
    # searchable_fields = ["name", ]
    # specifications = {
    #     "name": "__icontains"
    # }


def delete_content(request, content):
    get_content = Content.objects.filter(id=content).first()
    get_category = get_content.type.name
    get_content.delete()
    if get_category == "NEWS":
        messages.success(request, 'Deleted successfully')

        return redirect('WEB:news_list')
    elif get_category == "EVENT":
        messages.success(request, 'Deleted successfully')
        return redirect('WEB:event_list')
    elif get_category == "REPORT":
        messages.success(request, 'Deleted successfully')
        return redirect('WEB:report_list')
    elif get_category == "DOWNLOADS":
        messages.success(request, 'Deleted successfully')
        return redirect('WEB:downloads_list')
    elif get_category == "NEWS LETTER":
        messages.success(request, 'Deleted successfully')
        return redirect('WEB:news_letter_list')


def delete_programme(request, programme):
    get_content = Programme.objects.filter(id=programme).first()
    get_content.delete()

    messages.success(request, 'Deleted successfully')

    return redirect('WEB:programme_list')
