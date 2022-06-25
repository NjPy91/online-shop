# Generated by Django 3.2 on 2022-06-25 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name': 'ProductType', 'verbose_name_plural': 'ProductType'},
        ),
        migrations.AddField(
            model_name='producttype',
            name='create_time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttype',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='producttype',
            name='modified_time',
            field=models.TimeField(auto_now=True),
        ),
    ]