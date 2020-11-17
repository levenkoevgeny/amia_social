from django.shortcuts import render
from django.views import View
from .models import SocialProfile
from django.shortcuts import get_object_or_404
from .forms import RegistrationForm, ProfileForm, PersonalDataForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import transaction
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, View):
    def get(self, request, profile_id):
        profile_data = get_object_or_404(SocialProfile, pk=profile_id)
        return render(request, 'social_profile/profile.html', {
            'profile': profile_data
        })

    def post(self, request, profile_id):
        pass


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request, profile_id):
        obj = get_object_or_404(SocialProfile, pk=profile_id)
        form = ProfileForm(instance=obj)
        return render(request, 'social_profile/profile_update_form.html', {'form': form,
                                                                           'obj': obj,
                                                                           })


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
            return HttpResponseRedirect(reverse('institution:search'))
        else:
            return render(request, 'registration/registration.html', {'form': form})


def personal_data_update(request, profile_id):
    if request.method == 'POST':
        obj = get_object_or_404(SocialProfile, pk=profile_id)
        form = PersonalDataForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return JsonResponse({'last_name': request.POST['last_name'],
                                 'first_name': request.POST['first_name'],
                                 'email': request.POST['email'],
                                 'contact_information_phone': request.POST['contact_information_phone'],
                                 'contact_information_address': request.POST['contact_information_address'],
                                 'date_of_birth': request.POST['date_of_birth'],
                                 'patronymic': request.POST['patronymic'],
                                 'about_myself': request.POST['about_myself'],
                                 }, safe=False)
        else:
            return JsonResponse({'': ''}, safe=False)
    else:
        obj = get_object_or_404(SocialProfile, pk=profile_id)
        personal_data_form = PersonalDataForm(instance=obj)
        return render(request, 'social_profile/update/personal_data.html', {
            'form': personal_data_form,
            'obj': obj
        })
