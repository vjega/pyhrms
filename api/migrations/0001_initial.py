# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=20)),
                ('year_of_passing', models.CharField(default=b'', max_length=10)),
                ('doj', models.DateField(null=True, blank=True)),
                ('dor', models.DateField(null=True, blank=True)),
                ('designation', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=100)),
                ('father', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(max_length=1024)),
                ('temporary_address', models.CharField(max_length=1024)),
                ('email_id', models.EmailField(max_length=75)),
                ('pan_no', models.CharField(max_length=20)),
                ('passport_no', models.CharField(max_length=50)),
                ('dob', models.DateField(null=True, blank=True)),
                ('blood_group', models.CharField(max_length=20)),
                ('emergency_contact', models.CharField(max_length=100)),
                ('primary_contact', models.CharField(max_length=100)),
                ('secondary_contact', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('msys_reference', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=20)),
                ('msys_email', models.EmailField(max_length=75)),
                ('employees_number', models.CharField(max_length=20)),
                ('emails', models.EmailField(max_length=75)),
                ('acount_no', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employee',
            },
            bases=(models.Model,),
        ),
    ]
