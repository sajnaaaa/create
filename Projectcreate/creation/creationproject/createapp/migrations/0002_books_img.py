# Generated by Django 4.1.3 on 2022-11-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='img',
            field=models.ImageField(default='sajjjjj', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
