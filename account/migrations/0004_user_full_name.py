# Generated by Django 4.0.3 on 2022-09-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام کامل'),
        ),
    ]
