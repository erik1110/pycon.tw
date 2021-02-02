# Generated by Django 3.0.7 on 2021-01-31 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0018_openrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017'), ('pycontw-2018', 'PyCon Taiwan 2018'), ('pycontw-2019', 'PyCon Taiwan 2019'), ('pycontw-2020', 'PyCon Taiwan 2020'), ('pycontw-2021', 'PyCon Taiwan 2021')], default='pycontw-2021', verbose_name='conference'),
        ),
    ]
