# Generated by Django 3.2 on 2021-05-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_alter_medico_especialidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
