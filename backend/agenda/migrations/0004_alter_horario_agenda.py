# Generated by Django 3.2 on 2021-05-08 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_rename_horarios_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='agenda.agenda'),
        ),
    ]
