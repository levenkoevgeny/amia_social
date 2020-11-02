from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    language_name = models.CharField(max_length=100, verbose_name="Language_name")

    def __str__(self):
        return self.language_name

    class Meta:
        ordering = ('language_name',)
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class LanguageLevel(models.Model):
    LEVELS = (
        (1, 'Beginner'),
        (2, 'Pre-Intermediate'),
        (3, 'Intermediate'),
        (4, 'Upper-Intermediate'),
        (5, 'Advanced'),
        (6, 'Proficiency'),
    )
    language_level = models.IntegerField(verbose_name="language_level", choices=LEVELS)

    def __str__(self):
        return str(self.language_level)

    class Meta:
        ordering = ('language_level',)
        verbose_name = 'Language level'
        verbose_name_plural = 'Language levels'


class SocialProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    first_name = models.CharField(max_length=100, verbose_name="First name")
    patronymic = models.CharField(max_length=100, verbose_name="Patronymic", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Date_of_birth", blank=True, null=True)
    status = models.IntegerField(verbose_name="Status", default=1)
    date_added = models.DateTimeField(verbose_name="Date_added", auto_now_add=True)
    profile_img = models.ImageField(verbose_name="Profile_img", blank=True, null=True, upload_to='profile')
    about_myself = models.TextField(verbose_name="About_myself", blank=True, null=True)
    # contact_information =
    # education =
    # work_experience =
    interests = models.TextField(verbose_name="Interests", blank=True, null=True)
    skills = models.TextField(verbose_name="Skills", blank=True, null=True)
    languages = models.ManyToManyField(Language, verbose_name="Language", through='LanguageWithLevel')

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Social profile'
        verbose_name_plural = 'Social profiles'


class LanguageWithLevel(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    level = models.ForeignKey(LanguageLevel, on_delete=models.CASCADE)
