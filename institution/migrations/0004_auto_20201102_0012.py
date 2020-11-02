# Generated by Django 3.1.2 on 2020-11-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_profile', '0001_initial'),
        ('institution', '0003_auto_20201101_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='status',
            field=models.IntegerField(choices=[(1, 'Opened'), (2, 'Completed'), (3, 'Blocked')], default=1, verbose_name='Responded'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.CreateModel(
            name='RespondedVacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_response', models.DateTimeField(auto_now_add=True, verbose_name='Date of response')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.socialprofile')),
                ('vacansy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='vacancy',
            name='responded',
            field=models.ManyToManyField(through='institution.RespondedVacancy', to='social_profile.SocialProfile', verbose_name='Responded'),
        ),
    ]