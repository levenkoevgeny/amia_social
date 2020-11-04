from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from institution.models import Vacancy

from social_profile.models import SocialProfile


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        vacancies = Vacancy.objects.all()

        return render(request, 'institution/vacancies/hr_main_vacancies.html', {
            'vacancies': vacancies
        })


class ProfilesView(LoginRequiredMixin, View):

    def get(self, request):
        profiles = SocialProfile.objects.all()

        return render(request, 'hr/profiles/profiles.html', {
            'profiles': profiles
        })