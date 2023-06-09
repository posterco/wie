# Generated by Django 4.1 on 2023-05-23 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_alter_clubs_club_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='event_desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='event_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='events',
            name='event_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserEvents',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_user', to=settings.AUTH_USER_MODEL)),
                ('user_events', models.ManyToManyField(blank=True, to='accounts.events')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserClubs',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_user', to=settings.AUTH_USER_MODEL)),
                ('user_clubs', models.ManyToManyField(blank=True, null=True, to='accounts.clubs')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
