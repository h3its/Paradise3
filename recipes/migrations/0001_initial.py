# Generated by Django 4.1.1 on 2022-12-16 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe_Post',
            fields=[
                ('Post_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Body', models.TextField()),
                ('Date', models.DateField(auto_now_add=True)),
                ('Image', models.CharField(max_length=100)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
        ),
    ]