# Generated by Django 3.2.9 on 2021-12-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_alter_blogpost_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='excerpt',
            field=models.TextField(max_length=150, null=True),
        ),
    ]