# Generated by Django 4.1.3 on 2022-11-24 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0005_post_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
    ]
