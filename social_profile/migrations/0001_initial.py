# Generated by Django 3.1.3 on 2020-11-26 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institutional_name', models.CharField(max_length=255, verbose_name='Institutional name')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
                'ordering': ('institutional_name',),
            },
        ),
        migrations.CreateModel(
            name='EducationWithInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_entrance', models.IntegerField(verbose_name='Year of entrance')),
                ('year_of_graduating', models.IntegerField(blank=True, null=True, verbose_name='Year of graduating')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_name', models.CharField(max_length=255, verbose_name='Interest')),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
                'ordering': ('interest_name',),
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100, verbose_name='Language_name')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ('language_name',),
            },
        ),
        migrations.CreateModel(
            name='LanguageLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_level', models.IntegerField(choices=[(1, 'Beginner'), (2, 'Pre-Intermediate'), (3, 'Intermediate'), (4, 'Upper-Intermediate'), (5, 'Advanced'), (6, 'Proficiency')], verbose_name='language_level')),
            ],
            options={
                'verbose_name': 'Language level',
                'verbose_name_plural': 'Language levels',
                'ordering': ('language_level',),
            },
        ),
        migrations.CreateModel(
            name='LanguageWithLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.language')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.languagelevel')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=255, verbose_name='Skill')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
                'ordering': ('skill_name',),
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='Company name')),
                ('position', models.CharField(max_length=255, verbose_name='Position')),
                ('duty', models.TextField(blank=True, null=True, verbose_name='Duty')),
                ('year_start', models.IntegerField(verbose_name='Start year')),
                ('year_end', models.IntegerField(blank=True, null=True, verbose_name='End year')),
            ],
            options={
                'verbose_name': 'Work experience',
                'verbose_name_plural': 'Work experience',
                'ordering': ('-year_start',),
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty_name', models.CharField(max_length=255, verbose_name='Specialty name')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.educationalinstitution', verbose_name='Education')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
                'ordering': ('specialty_name',),
            },
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Patronymic')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date_of_birth')),
                ('status', models.IntegerField(default=1, verbose_name='Status')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date_added')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='Profile_img')),
                ('about_myself', models.TextField(blank=True, null=True, verbose_name='About_myself')),
                ('contact_information_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('contact_information_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('education', models.ManyToManyField(through='social_profile.EducationWithInfo', to='social_profile.Specialty', verbose_name='Education')),
                ('interests', models.ManyToManyField(blank=True, to='social_profile.Interest', verbose_name='Interests')),
                ('languages', models.ManyToManyField(through='social_profile.LanguageWithLevel', to='social_profile.Language', verbose_name='Language')),
                ('skills', models.ManyToManyField(blank=True, to='social_profile.Skill', verbose_name='Skills')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('work_experience', models.ManyToManyField(to='social_profile.WorkExperience', verbose_name='Work experience')),
            ],
            options={
                'verbose_name': 'Social profile',
                'verbose_name_plural': 'Social profiles',
                'ordering': ('last_name',),
            },
        ),
        migrations.AddField(
            model_name='languagewithlevel',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.socialprofile'),
        ),
        migrations.AddField(
            model_name='educationwithinfo',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.socialprofile'),
        ),
        migrations.AddField(
            model_name='educationwithinfo',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_profile.specialty'),
        ),
    ]
