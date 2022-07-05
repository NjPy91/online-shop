from django.urls import path
from catalogue.views import *



urlpatterns = [
    path('category/list/', categoty_list, name='category-list')

]