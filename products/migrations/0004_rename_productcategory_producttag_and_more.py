# Generated by Django 4.2.5 on 2023-09-08 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cartitem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductCategory',
            new_name='ProductTag',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='tags',
        ),
    ]
