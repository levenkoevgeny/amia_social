from django.shortcuts import render
from django.views import View
from .models import SocialProfile
from django.shortcuts import get_object_or_404


class ProfileView(View):
    def get(self, request, profile_id):
        profile_data = get_object_or_404(SocialProfile, pk=profile_id)
        return render(request, 'social_profile/profile.html', {
            'profile': profile_data
        })

    def post(self, request):
        pass
