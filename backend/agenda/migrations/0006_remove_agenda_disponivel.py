# Generated by Django 3.2 on 2021-05-13 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_agenda_disponivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='disponivel',
        ),
    ]
