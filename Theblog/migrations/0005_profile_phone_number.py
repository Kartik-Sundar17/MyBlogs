# Generated by Django 5.0.6 on 2024-06-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Theblog', '0004_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]