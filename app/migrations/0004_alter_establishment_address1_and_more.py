# Generated by Django 4.1.4 on 2023-05-09 16:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_establishment_rating_alter_establishment_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='establishment',
            name='address1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='address2',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='contact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='district',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='pin',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='rating',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='state',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='establishment',
            name='street',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.TextField(null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, null=True, verbose_name='phone'),
        ),
    ]
