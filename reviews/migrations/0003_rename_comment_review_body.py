# Generated by Django 4.2.16 on 2024-10-26 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='body',
        ),
    ]
