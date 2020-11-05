from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Institution, Vacancy, LanguageWithLevelVacancy
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import VacancyFilterForProfile
from django.core.paginator import Paginator
from .forms import VacancyForm, LanguageWithLevelVacancyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction


class SearchView(LoginRequiredMixin, View):
    def get(self, request):
        institutions = Institution.objects.all()
        vacancies = Vacancy.objects.all().order_by('-date_added')[:5]

        f = VacancyFilterForProfile(request.GET, queryset=Vacancy.objects.all().order_by('-pk'))
        paginator = Paginator(f.qs, 50)
        page = request.GET.get('page')
        vacancies_search = paginator.get_page(page)

        return render(request, 'institution/vacancies/vacancy_search.html', {
            'institutions': institutions,
            'vacancies': vacancies,
            'vacancies_search': vacancies_search,
            'filter': f,
        })


class InstitutionVacancyView(View):
    def get(self, request, institution_id):
        institution = get_object_or_404(Institution, pk=institution_id)
        return render(request, 'institution/vacancies/vacancy_institution.html', {
            'institution': institution,
        })

    def post(self, request):
        pass


class VacancyAddView(View):

    def get(self, request):
        form_main = VacancyForm
        form_language = LanguageWithLevelVacancyForm
        return render(request, 'institution/vacancies/vacancy_input_form.html', {
            'form': form_main,
            'form_language': form_language,
        })

    @transaction.atomic
    def post(self, request):
        form = VacancyForm(request.POST)
        form_language = LanguageWithLevelVacancyForm(request.POST)
        if form.is_valid() and form_language.is_valid():
            vacancy_new = form.save()
            language_with_level = form_language.save(commit=False)
            language_with_level.vacancy = vacancy_new
            language_with_level.save()
            return HttpResponseRedirect(reverse('hr:main'))
        else:
            return render(request, 'institution/vacancies/vacancy_input_form.html', {
                'form': form, 'form_language': form_language
            })


class VacancyUpdateView(View):
    def get(self, request, vacancy_id):
        obj = get_object_or_404(Vacancy, pk=vacancy_id)
        lang_obj = LanguageWithLevelVacancy.objects.filter(vacancy_id=obj.id).first()
        form = VacancyForm(instance=obj)
        form_language = LanguageWithLevelVacancyForm(instance=lang_obj)
        return render(request, 'institution/vacancies/vacancy_update_form.html', {
            'form': form,
            'form_language': form_language,
            'obj': obj,
        })

    @transaction.atomic
    def post(self, request, vacancy_id):
        obj = get_object_or_404(Vacancy, pk=vacancy_id)
        lang_obj = LanguageWithLevelVacancy.objects.filter(vacancy_id=obj.id).first()
        form = VacancyForm(request.POST, instance=obj)
        form_language = LanguageWithLevelVacancyForm(request.POST, instance=lang_obj)
        if form.is_valid() and form_language.is_valid():
            vacancy_new = form.save()
            language_with_level = form_language.save(commit=False)
            language_with_level.vacancy = vacancy_new
            language_with_level.save()
            return HttpResponseRedirect(reverse('hr:main'))
        else:
            return render(request, 'institution/vacancies/vacancy_input_form.html', {
                'form': form, 'form_language': form_language
            })

