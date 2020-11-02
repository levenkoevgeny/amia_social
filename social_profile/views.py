from django.shortcuts import render
from django.views import View
from .models import SocialProfile
from django.shortcuts import get_object_or_404
from .forms import RegistrationForm, ProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction


class ProfileView(View):
    def get(self, request, profile_id):
        profile_data = get_object_or_404(SocialProfile, pk=profile_id)
        return render(request, 'social_profile/profile.html', {
            'profile': profile_data
        })

    def post(self, request):
        pass


class ProfileUpdateView(View):
    def get(self, request, profile_id):
        obj = get_object_or_404(SocialProfile, pk=profile_id)
        form = ProfileForm(instance=obj)
        return render(request, 'social_profile/profile_update_form.html', {'form': form,
                                                                           'obj': obj,
                                                                           })

    def post(self, request):
        pass


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm
        return render(request, 'registration/registration.html', {
            'form': form
        })

    @transaction.atomic
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            profile_user = User.objects.create_user(
                request.POST['username'],
                request.POST['email'],
                request.POST['password']
            )

            profile = SocialProfile(
                user=profile_user,
                last_name=request.POST['last_name'],
                first_name=request.POST['first_name'],
                email=request.POST['email']
            )

            profile.save()
            profile.user = profile_user

            return HttpResponseRedirect(reverse('profile:profile_registration'))
        else:
            return render(request, 'registration/registration.html', {'form': form})