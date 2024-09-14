# Generated by Django 5.1.1 on 2024-09-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('date_applied', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
