# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('get_profile_list/', views.get_profile_list, name='get_profile_list'),
    path('add_company/', views.add_company, name='add_company'),
    path('switch_language/', views.switch_language, name='switch_language'),
    path('switch_profile/', views.switch_profile, name='switch_profile'),
    path('user/', views.user_profile, name='user_profile'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
