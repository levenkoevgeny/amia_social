from django.contrib import admin
from .models import Language, LanguageLevel, SocialProfile, LanguageWithLevel

admin.site.register(Language)
admin.site.register(LanguageLevel)
admin.site.register(SocialProfile)
admin.site.register(LanguageWithLevel)