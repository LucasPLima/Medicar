# Generated by Django 3.2 on 2021-05-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_alter_horario_agenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
