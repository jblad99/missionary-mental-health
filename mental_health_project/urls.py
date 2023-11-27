# mental_health_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mental_health/', include('mental_health_app.urls')),
]
