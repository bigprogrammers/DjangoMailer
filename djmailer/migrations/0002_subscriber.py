# Generated by Django 5.1.4 on 2024-12-26 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djmailer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('email_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='djmailer.emaillist')),
            ],
        ),
    ]
