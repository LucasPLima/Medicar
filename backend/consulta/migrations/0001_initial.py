# Generated by Django 3.2 on 2021-05-13 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medico', '0004_alter_medico_email'),
        ('agenda', '0005_agenda_disponivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_agendamento', models.DateField(auto_now_add=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.agenda')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.horario')),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico.medico')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
