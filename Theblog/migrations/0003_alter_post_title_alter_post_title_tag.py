# Generated by Django 5.0.6 on 2024-06-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theblog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(max_length=2000),
        ),
    ]