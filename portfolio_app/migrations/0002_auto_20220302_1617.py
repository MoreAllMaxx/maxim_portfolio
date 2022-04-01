# Generated by Django 2.2 on 2022-03-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='name'),
        ),
    ]