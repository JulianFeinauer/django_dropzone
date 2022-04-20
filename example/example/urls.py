"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve

import django_dropzone.views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", django_dropzone.views.DropzoneIndex.as_view()),
    path("uploads", csrf_exempt(django_dropzone.views.UploadView.as_view())),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    ]