# Generated by Django 3.0.5 on 2020-05-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200505_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='informations',
        ),
        migrations.RemoveField(
            model_name='person',
            name='isOrganizer',
        ),
        migrations.AddField(
            model_name='person',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='birthDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='language',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='postalCode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='bio',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='sex',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
