from django.urls import path

from . import views


#
# URLS are basically urls that will attach to a method in views which will render a template for that method
# params: url name, method inside view file, then the name of the method
# 


urlpatterns = [
    path('', views.index, name="listings"),
    path('<int:listing_id>', views.listing, name="listing"),
    path('search', views.search, name="search")
]