# Generated by Django 3.0 on 2024-04-21 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_auto_20240420_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicines',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='symptoms',
            name='minimum_age',
        ),
        migrations.AddField(
            model_name='medicines',
            name='brand',
            field=models.CharField(default='Generic', max_length=10, verbose_name='Marca'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicines',
            name='laboratory',
            field=models.CharField(default='Generic', max_length=10, verbose_name='Laboratorio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='medicines',
            name='description',
            field=models.CharField(max_length=256, verbose_name='Descripcion del medicamento'),
        ),
        migrations.AlterField(
            model_name='medicines',
            name='image',
            field=models.ImageField(blank=True, upload_to='medicines', verbose_name='Imagen'),
        ),
        migrations.RemoveField(
            model_name='medicines',
            name='symptom',
        ),
        migrations.AddField(
            model_name='medicines',
            name='symptom',
            field=models.ManyToManyField(to='medicines.Symptoms', verbose_name='Sintoma'),
        ),
    ]