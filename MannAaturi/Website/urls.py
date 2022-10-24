"""MannAaturi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Website import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('contact', views.Contact),
    path('sending', views.Sending_Message),
    path('signup', views.Signup),
    path('signing-up', views.Signing_In),
    path('login', views.Login),
    path('logging-in', views.Logging_In),
    path('logout', views.Logout),
    path('videos', views.Videos),
    path('pdfs', views.PDF),
    path('search', views.Search),
    path('search_pdf', views.Search_PDF),
    re_path(r'^download/(?P<path>.*)$',serve, {'document_root' : settings.MEDIA_ROOT}),
]
