# Generated by Django 4.1.1 on 2022-10-05 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]