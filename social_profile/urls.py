from django.urls import path
from . import views
# from django.contrib.auth.decorators import permission_required

app_name = 'profile'

urlpatterns = [
    path('<profile_id>/', views.ProfileView.as_view(), name='profile_data'),
    path('new/registration/', views.RegistrationView.as_view(), name='profile_registration'),
    path('update/<profile_id>/', views.ProfileUpdateView.as_view(), name='profile_update'),
    path('update/personal_data/<profile_id>/', views.personal_data_update, name='profile_update_personal_data')
    # path('', views.sciencework_list, name='list'),
    # path('add/', permission_required('sciencework.add_sciencework')(views.sciencework_add), name='add'),
    # path('update/<sciencework_id>/change/', permission_required('sciencework.change_sciencework')(views.sciencework_update), name='update'),
    # path('delete/<pk>/', permission_required('sciencework.delete_sciencework')(views.ScienceworkDelete.as_view()), name='delete'),
]