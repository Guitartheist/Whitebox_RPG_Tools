# Generated by Django 3.1.7 on 2022-01-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitebox', '0004_meleeweapon'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='melee_weapons',
            field=models.ManyToManyField(blank=True, to='whitebox.MeleeWeapon'),
        ),
    ]
