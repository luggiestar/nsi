from django.shortcuts import render


def index_view(request):
    return render(request, "website/home2.html")