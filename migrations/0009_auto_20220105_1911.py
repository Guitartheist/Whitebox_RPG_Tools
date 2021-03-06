# Generated by Django 3.1.7 on 2022-01-06 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whitebox', '0008_auto_20220104_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='RangedWeapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('damage', models.CharField(max_length=40)),
                ('weight', models.IntegerField()),
                ('rof', models.FloatField()),
                ('w_range', models.IntegerField()),
                ('cost_gp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RangedWeaponQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='raned_weapon_quantity', to='whitebox.character')),
                ('melee_weapon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ranged_weapon_quantity', to='whitebox.rangedweapon')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='ranged_weapons',
            field=models.ManyToManyField(related_name='ranged_weapons', through='whitebox.RangedWeaponQuantity', to='whitebox.RangedWeapon'),
        ),
    ]
