# Generated by Django 4.0 on 2024-11-16 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_topics'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='topics',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='types',
            options={'ordering': ['name']},
        ),
    ]
