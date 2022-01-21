# Generated by Django 2.2.5 on 2019-09-15 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('date_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_ended', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('callee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='callee_user', to=settings.AUTH_USER_MODEL)),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caller_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
