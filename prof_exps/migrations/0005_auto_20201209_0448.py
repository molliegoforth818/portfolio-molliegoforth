# Generated by Django 3.0.5 on 2020-12-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof_exps', '0004_about_me_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
    ]