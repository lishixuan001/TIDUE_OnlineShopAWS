# Generated by Django 3.1.2 on 2020-11-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_remove_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='number',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
