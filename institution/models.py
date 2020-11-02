from django.db import models
from django.contrib.auth.models import User
from social_profile.models import SocialProfile


class Institution(models.Model):
    institution_name = models.CharField(max_length=255, verbose_name="Institution name")

    def __str__(self):
        return self.institution_name

    class Meta:
        ordering = ('institution_name',)
        verbose_name = 'Institution'
        verbose_name_plural = 'Institution'


class Vacancy(models.Model):
    OPENED = 1
    COMPLETED = 2
    BLOCKED = 3

    STATUSES = [
        (OPENED, 'Opened'),
        (COMPLETED, 'Completed'),
        (BLOCKED, 'Blocked'),
    ]
    vacancy = models.CharField(max_length=255, verbose_name="Vacancy")
    date_added = models.DateTimeField(verbose_name="Date added", auto_now_add=True)
    who_added = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Who added", blank=True, null=True)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, verbose_name="Institution")
    responded = models.ManyToManyField(SocialProfile, verbose_name="Responded", through='RespondedVacancy')
    status = models.IntegerField(verbose_name="Responded", choices=STATUSES, default=OPENED)

    def __str__(self):
        return self.vacancy

    class Meta:
        ordering = ('vacancy',)
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class RespondedVacancy(models.Model):
    profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    vacansy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date_of_response = models.DateTimeField(verbose_name="Date of response", auto_now_add=True)