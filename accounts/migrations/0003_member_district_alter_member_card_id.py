# Generated by Django 4.0.1 on 2023-07-24 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_member_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='district',
            field=models.CharField(default='Kaliro', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='card_id',
            field=models.IntegerField(verbose_name='Membership card id'),
        ),
    ]
