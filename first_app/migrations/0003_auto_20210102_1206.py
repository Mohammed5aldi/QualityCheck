# Generated by Django 2.2.4 on 2021-01-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20210102_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chacks',
            name='breast_bruises',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='breast_laceration',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='breast_skin_lesion',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='feet_ammonia_burn',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='legs_bruises',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='legs_fractures',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='legs_old_injury',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='legs_scrach',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='machine_damage',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='wing_broken',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='wing_bruises',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='chacks',
            name='wing_dislocation',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
