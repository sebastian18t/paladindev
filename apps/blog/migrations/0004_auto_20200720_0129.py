# Generated by Django 3.0.8 on 2020-07-20 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
