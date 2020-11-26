# Generated by Django 3.1.3 on 2020-11-26 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_name', models.CharField(max_length=255, verbose_name='Название чата')),
                ('chat_type', models.IntegerField(choices=[(1, 'Personal'), (2, 'Group')], default=1, verbose_name='Тип чата')),
            ],
            options={
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
                'ordering': ('chat_name',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField(verbose_name='Текст сообщения')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время сообщения')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messaging.chat', verbose_name='Название чата')),
                ('message_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Message_from', to='social_profile.socialprofile', verbose_name='Сообщение от')),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Message_to', to='social_profile.socialprofile', verbose_name='Сообщение к')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channels_name', models.TextField(verbose_name='Имя канала')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ('client',),
            },
        ),
    ]
