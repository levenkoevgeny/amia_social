from django.urls import path
from . import views

app_name = 'institution'

urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
    path('<institution_id>/vacancy', views.InstitutionVacancyView.as_view(), name='institution_vacancy'),
    path('vacancy/add/', views.VacancyAddView.as_view(), name='vacancy_add'),
    path('vacancy/<institution_id>/update/', views.VacancyUpdateView.as_view(), name='vacancy_update')
]