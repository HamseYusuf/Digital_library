# Generated by Django 4.2.7 on 2023-11-20 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='category_name',
            new_name='school_name',
        ),
    ]
