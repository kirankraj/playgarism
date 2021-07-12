"""plagiarism URL Configuration

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
from django.urls import path

from django.contrib import admin
from django.urls import path
from common import __views
from app import views
__views.MODELS_PATH = 'app.models'
urlpatterns = [
    path('', views.index),
    path('view/<page>', __views.__view),
    path('all/<model>/<keyvalue>/<page>', __views.__all),#username=1&password=123|name=7
    # path('table/<model>/<page>', __views.__table),
    # path('get/<model>/<key>/<value>/<page>', __views.__get),
    path('form/<model>/<page>', __views.__form),
    # path('form/<model>/<listmodel>/<page>', __views.__form_list),
    path('edit/<model>/<id>/<page>', __views.__edit),
    # path('edit/<model>/<id>/<listmodel>/<page>', __views.__edit_list),
    path('delete/<model>/<id>', __views.__delete),
    path('save', __views.__save),
    path('login', views.login),
    path('logout', views.logout),
    path('check',views.check),
    path('viewmore',views.viewmore),
    path('approve',views.approve),
    path('upload',views.upload),
    path('detail', views.detail),
    path('teacherdetail', views.teacherdetail),
    path('contact', views.contact)


]