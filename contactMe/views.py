from django.shortcuts import render
from .forms import ContactMeForm


def contactMe_index(request):
    form = ContactMeForm(request.POST or None)
    if form.is_valid():
        print(form.data)
        form.save()
        form = ContactMeForm()
    context = {
        'form': form
    }
    return render(request, "contactMe_index.html", context)
