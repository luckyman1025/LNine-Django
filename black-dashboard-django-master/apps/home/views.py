# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import translation

from .forms import UserProfileForm
from .models import UserProfile

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def user_profile(request):  

    user_profile = UserProfile.objects.get(user=request.user, is_active=True)
    language = user_profile.language
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

    context = {'segment': 'user_profile', 'language': language}
    # html_template = loader.get_template('home/user.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/user.html', context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# @login_required(login_url="/login/")
def get_profile_list(request):
    print("123123123123123123123213123")
    
    user_profiles = UserProfile.objects.filter(user=request.user)
    print(user_profiles)

    user_profile = UserProfile.objects.get(user=request.user, is_active=True)
    language = user_profile.language
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language

    user_profiles_list = []
    for profile in user_profiles:
        profile_dict = {
            'id': profile.id,
            'profile': profile.profile,
            'is_active': profile.is_active,
            'language': profile.language,
            'company': {
                'id': profile.company.id if profile.company else None,
                'name': profile.company.name if profile.company else None,
                'location': profile.company.location if profile.company else None
            }
        }
        user_profiles_list.append(profile_dict)

    context = {
        'user_profiles': user_profiles_list,
        'language': language,
        'segment': 'user_profile'
    }

    # return render(request, 'home/user.html', context)
    return JsonResponse(context)
    # user_profiles_list = list(user_profiles.values('id', 'profile', 'is_active', 'language', 'company'))

    # context = {
    #     'user_profiles': user_profiles_list,
    #     'language': language,
    #     'segment': 'user_profile'
    # }

    # return JsonResponse(context)

@login_required
def add_company(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        
        print(name)
        print(location)

        company = Company.objects.create(
            name=name,
            location=location
        )
        
        UserProfile.objects.create(
            user=request.user,
            company=company
        )
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required(login_url="/login/")
def switch_profile(request):

    if request.method == 'POST':

        profile_id = request.POST.get('profile_id')
        # Deactivate all user profiles
        UserProfile.objects.filter(user=request.user).update(is_active=False)
        
        # Activate selected profile
        profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
        profile.is_active = True
        profile.save()
        
        return render(request, 'home/index.html', {'status': 'success'})
    return render(request, 'home/index.html', {'status': 'error'})



@login_required
def switch_language(request):


    print(">>>>>>>>>>>")
    if request.method == 'POST':
        language = request.POST.get('language', 'en')
        if language in [lang[0] for lang in settings.LANGUAGES]:
            if request.user.is_authenticated:
                request.user.language = language
                request.user.save()
            translation.activate(language)
            request.session[translation.LANGUAGE_SESSION_KEY] = language
    
    profile = get_object_or_404(UserProfile, is_active=True, user=request.user)
    profile.language = language
    profile.save()

    print("language", language)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    


