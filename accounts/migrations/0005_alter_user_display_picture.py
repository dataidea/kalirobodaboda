# Generated by Django 4.0.1 on 2023-07-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_picture',
            field=models.ImageField(default='images/smily.jpg', upload_to=''),
        ),
    ]