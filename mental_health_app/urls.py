# in urls.py

from django.urls import path
from .views import home, missionary_form, missionary_detail, resources, success_page, missionary_responses

urlpatterns = [
    path('', home, name='home'),
    path('missionary/form/', missionary_form, name='missionary_form'),
    path('missionary/success_page/', success_page, name='success_page'),
    path('missionary/responses/', missionary_responses, name='missionary_responses'),
    path('missionary/detail/<int:pk>/', missionary_detail, name='missionary_detail'),
    path('missionary/resources/', resources, name='resources'),
]
