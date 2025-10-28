from django.urls import path

from . import views


#
# URLS are basically urls that will attach to a method in views which will render a template for that method
# params: url name, method inside view file, then the name of the method
# 


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about")
]