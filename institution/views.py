from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Institution, Vacancy
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import VacancyFilterForProfile
from django.core.paginator import Paginator


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


    def post(self, request):
        pass


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
        return render(request, 'institution/vacancies/vacancy_input_form.html')

    def post(self, request):
        pass


class VacancyUpdateView(View):
    def get(self, request, vacancy_id):
        return render(request, 'institution/vacancies/vacancy_update_form.html')

    def post(self, request, institution_id):
        pass
