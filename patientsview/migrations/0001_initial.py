# Generated by Django 3.2 on 2021-07-10 08:49

from django.db import migrations, models
import patientsview.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default='uploads/images/patients/icon.png', upload_to=patientsview.models.upload_path)),
                ('patient_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('account_created_hospital_id', models.CharField(max_length=100)),
                ('app_id', models.CharField(max_length=30, unique=True)),
                ('address', models.CharField(default='', max_length=250)),
                ('mobile_no', models.CharField(max_length=20, null=True, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('aadhar_number', models.CharField(default='', max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('mobile_verified', models.BooleanField(default=False)),
                ('otp_code', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PatientsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=100)),
                ('aadhar_number', models.CharField(default='', max_length=30)),
                ('doctor_id', models.CharField(max_length=100)),
                ('symptoms', models.TextField(null=True)),
                ('cause', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('revisit_date', models.DateField()),
                ('entered_date', models.DateTimeField(auto_now_add=True)),
                ('verified', models.BooleanField(default=False)),
                ('verify_token', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PatientsTestFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.CharField(max_length=100)),
                ('app_id', models.CharField(max_length=30)),
                ('tested_files', models.FileField(upload_to='')),
                ('doctor_id', models.CharField(max_length=100)),
                ('verified', models.BooleanField(default=False)),
                ('verify_token', models.CharField(max_length=255)),
                ('entered_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]