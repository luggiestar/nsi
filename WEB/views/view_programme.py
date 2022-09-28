from django.shortcuts import render, get_object_or_404
from WEB.models.user import Programme


def view_programme(request, id):
    get_programme = get_object_or_404(Programme, pk=id)
    context = {
        'programme': get_programme
    }
    return render(request, "WEB/view_programme.html", context)
