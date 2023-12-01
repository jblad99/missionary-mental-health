# mental_health_app/views.py
from django.shortcuts import render, redirect
from .forms import MissionaryForm
from .models import Missionary, Response
from django.core.serializers import serialize

def missionary_form(request):
    if request.method == 'POST':
        form = MissionaryForm(request.POST)
        if form.is_valid():
            # Set the rating field to the mood slider value
            form.instance.rating = form.cleaned_data['rating']
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = MissionaryForm()

    return render(request, 'mental_health_app/missionary_form.html', {'form': form})

def success_page(request):
    return render(request, 'mental_health_app/success_page.html')

def missionary_responses(request):
    missionaries = Missionary.objects.all()
    json_data = serialize('json', missionaries)
    return render(request, 'mental_health_app/missionary_responses.html', {'missionaries': missionaries, 'asdf':json_data})

def missionary_detail(request, pk):
    missionary = Missionary.objects.get(pk=pk)
    return render(request, 'mental_health_app/missionary_detail.html', {'missionary': missionary})

def resources(request):
    return render(request, 'mental_health_app/resources.html')

def home(request):
    return render(request, 'mental_health_app/home.html')