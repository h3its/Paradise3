# Generated by Django 4.1.1 on 2022-10-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.CharField(max_length=100),
        ),
    ]
