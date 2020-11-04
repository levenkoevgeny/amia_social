from django.db import models
from django.contrib.auth.models import User
from social_profile.models import SocialProfile

from .tasks import send_email
from django.db.models.signals import post_save, pre_save


class Institution(models.Model):
    institution_name = models.CharField(max_length=255, verbose_name="Institution name")
    info_about = models.TextField(verbose_name="About", blank=True, null=True)
    img = models.ImageField(verbose_name="Image", blank=True, null=True, upload_to='institutions')
    subscribers = models.ManyToManyField(SocialProfile, verbose_name="Subscribers")

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
    status = models.IntegerField(verbose_name="Status", choices=STATUSES, default=OPENED)

    def __str__(self):
        return self.vacancy

    class Meta:
        ordering = ('vacancy',)
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def save(self, *args, **kwargs):
        if self.pk:
            created = False
        else:
            created = True
        super().save(*args, **kwargs)
        send_email.delay(self.institution.pk, self.pk, created)




        # institution = self.institution
        # if institution.subscribers:
        #     for subscriber in institution.subscribers.all():
        #         send_mail(
        #             'New positions!!!',
        #             self.vacancy,
        #             settings.EMAIL_HOST_USER,
        #             ['leva24031986@gmail.com'],
        #             fail_silently=False,
        #         )


class RespondedVacancy(models.Model):
    profile = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    vacansy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    date_of_response = models.DateTimeField(verbose_name="Date of response", auto_now_add=True)


# def save_profile(sender, instance, **kwargs):
#     print('signal', instance.pk)
#
#
# pre_save.connect(save_profile, sender=Vacancy)