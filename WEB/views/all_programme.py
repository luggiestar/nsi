from django.shortcuts import render, get_object_or_404
from WEB.models.user import Programme

def all_programme(request):
    programme_list = Programme.objects.all()
    serial = 1
    context = {
        'programme':programme_list,
        'serial': serial
    }
    return render(request, "WEB/all_programme.html", context)