from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('<profile_id>/', views.ProfileView.as_view(), name='profile_data'),
    path('new/registration/', views.RegistrationView.as_view(), name='profile_registration'),
    path('update/<profile_id>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('update/personal_data/<profile_id>/', views.personal_data_update, name='profile_update_personal_data'),
    path('education/add/', views.EducationAddView.as_view(), name='profile_education_add'),
    path('education/delete/<education_id>/', views.educationWithInfoDelete, name='profile_education_delete')
]