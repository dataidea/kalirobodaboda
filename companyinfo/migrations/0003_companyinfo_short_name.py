# Generated by Django 4.0.1 on 2023-07-31 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyinfo', '0002_rename_frequentlyaskedquestions_frequentlyaskedquestion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='short_name',
            field=models.CharField(default='test', max_length=25),
            preserve_default=False,
        ),
    ]
