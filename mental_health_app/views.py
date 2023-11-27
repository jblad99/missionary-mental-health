# mental_health_app/views.py
from django.shortcuts import render, redirect
from .forms import MissionaryForm
from .models import Missionary, Response

def missionary_form(request):
    if request.method == 'POST':
            form = MissionaryForm()
    else:
        form = MissionaryForm()

    return render(request, 'mental_health_app/missionary_form.html', {'form': form})
    #     form = MissionaryForm(request.POST)
    #     if form.is_valid():
    #         missionary = form.save()
    #         return redirect('missionary_detail', pk=missionary.pk)
    # else:
    #     form = MissionaryForm()
    # return render(request, 'mental_health_app/missionary_form.html', {'form': form})

def missionary_detail(request, pk):
    missionary = Missionary.objects.get(pk=pk)
    return render(request, 'mental_health_app/missionary_detail.html', {'missionary': missionary})

def resources(request):
    return render(request, 'mental_health_app/resources.html')

def home(request):
    return render(request, 'mental_health_app/home.html')