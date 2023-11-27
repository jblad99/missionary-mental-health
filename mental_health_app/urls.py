# in urls.py

from django.urls import path
from .views import home, missionary_form, missionary_detail, resources

urlpatterns = [
    path('', home, name='home'),
    path('missionary/form/', missionary_form, name='missionary_form'),
    path('missionary/detail/<int:pk>/', missionary_detail, name='missionary_detail'),
    path('missionary/resources/', resources, name='resources'),
]
