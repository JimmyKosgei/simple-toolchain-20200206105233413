# Generated by Django 2.2 on 2020-01-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('case_no', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='CASE_NO')),
                ('diagnosis', models.CharField(max_length=255)),
                ('treatment', models.CharField(max_length=255)),
                ('vet_remarks', models.CharField(max_length=255, null=True)),
                ('revisit_date', models.DateField(null=True)),
            ],
        ),
    ]
