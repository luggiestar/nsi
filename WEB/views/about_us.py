from contextvars import Context
from unicodedata import category
from django.shortcuts import render, get_object_or_404
from ..models import AboutUs


def about_us(request):
    history = get_object_or_404(AboutUs, category = "history")
    mission = get_object_or_404(AboutUs, category = "mission")
    function = get_object_or_404(AboutUs, category = "function")
    context = {
        'history_list':history,
        'function_list':function,
        'mission':mission,
    }
    return render(request, "WEB/about_us.html", context)