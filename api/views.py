from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def sample_view(request):
    data = {
        "message": "Hello from Django!"
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

