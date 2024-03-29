# Generated by Django 2.2 on 2019-05-28 18:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0002_plot_second_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOnCemetary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horizontal', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4, 'Miejsce wykracza poza mapę cmenta')])),
                ('vertical', models.IntegerField(validators=[django.core.validators.MaxValueValidator(4, 'Miejsce wykracza poza mapę cmentarza')])),
            ],
        ),
        migrations.DeleteModel(
            name='Plot',
        ),
        migrations.CreateModel(
            name='DeadPerson',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30, null=True)),
                ('surname', models.CharField(max_length=30)),
                ('birth_date', models.DateField(verbose_name='birth date')),
                ('death_date', models.DateField(verbose_name='death date')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='plots.PlaceOnCemetary')),
            ],
        ),
    ]
