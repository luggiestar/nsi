from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages

from ..forms import *
from ..models import *


def news_form(request):
    get_type = Type.objects.filter(name="NEWS").first()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.type = get_type
            get_form.save()
            messages.success(request, 'Saved Successfully')
        else:
            messages.error(request, 'Failed, image must be in .png or .jpg format')
            # return redirect('WEB:news_form')
    form = NewsForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/news_form.html', context)


def event_form(request):
    get_type = Type.objects.filter(name="EVENT").first()

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.type = get_type
            get_form.save()
            messages.success(request, 'Saved Successfully')

        else:
            messages.error(request, 'Failed, image must be in .png or .jpg format')

            return redirect('WEB:event_form')
    form = EventForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/event_form.html', context)


def news_letter_form(request):
    get_type = Type.objects.filter(name="NEWS LETTER").first()
    if request.method == "POST":
        form = NewsLetterForm(request.POST, request.FILES)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.type = get_type
            get_form.save()
            messages.success(request, 'saved successfully')

        else:
            messages.error(request, 'Failed, try again')

            return redirect('WEB:news_letter_form')
    form = NewsLetterForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/news_letter_form.html', context)


def upload_document_form(request):
    get_type = Type.objects.filter(name="DOWNLOADS").first()
    if request.method == "POST":
        form = DownloadForm(request.POST, request.FILES)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.type = get_type
            get_form.save()
            messages.success(request, 'The document saved successfully')



        else:
            messages.error(request, 'Failed, The document must be in a pdf format')
            return redirect('WEB:upload_document_form')
    form = DownloadForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/upload_document_form.html', context)


def report_form(request):
    get_type = Type.objects.filter(name="REPORT").first()
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            get_form = form.save(commit=False)
            get_form.type = get_type
            get_form.save()
            messages.success(request, 'The report saved successfully')


        else:
            messages.error(request, 'Failed, Report Must be in pdf format')
            return redirect('WEB:report_form')
    form = ReportForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/report_form.html', context)
def programme_form(request):
    # get_type = Type.objects.filter(name="REPORT").first()
    if request.method == "POST":
        form = ProgrammeForm(request.POST)
        if form.is_valid():
            # get_form = form.save(commit=False)
            get_form = form.save()
            # get_form.type = get_type
            # get_form.save()
            messages.success(request, 'The Programme saved successfully')


        else:
            messages.error(request, 'Failed, try again')
            return redirect('WEB:programme_form')
    form = ProgrammeForm()
    context = {
        'form': form,
    }
    return render(request, 'WEB/programme_form.html', context)


def update_news(request, object_pk):
    try:
        instance = Content.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:news_list')
    else:
        form = NewsForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/news_form.html', context_dict)


def update_event(request, object_pk):
    try:
        instance = Content.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = EventForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:event_list')
    else:
        form = EventForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/event_form.html', context_dict)


def update_news_letter(request, object_pk):
    try:
        instance = Content.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = NewsLetterForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:news_letter_list')
    else:
        form = NewsLetterForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/news_letter_form.html', context_dict)


def update_report(request, object_pk):
    try:
        instance = Content.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:report_list')
    else:
        form = ReportForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/report_form.html', context_dict)


def update_downloads(request, object_pk):
    try:
        instance = Content.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = DownloadForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:downloads_list')
    else:
        form = DownloadForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/upload_document_form.html', context_dict)


def update_programme(request, object_pk):
    try:
        instance = Programme.objects.get(id=object_pk)
    except Content.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = ProgrammeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('WEB:programme_list')
    else:
        form = ProgrammeForm(instance=instance)
    context_dict = {'form': form, 'instance': instance}
    return render(request, 'WEB/programme_form.html', context_dict)
