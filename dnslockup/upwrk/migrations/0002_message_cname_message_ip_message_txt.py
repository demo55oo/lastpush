# Generated by Django 4.0.6 on 2022-07-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upwrk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='cname',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='ip',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='txt',
            field=models.TextField(null=True),
        ),
    ]