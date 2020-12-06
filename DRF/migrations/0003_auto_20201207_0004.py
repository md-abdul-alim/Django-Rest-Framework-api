# Generated by Django 3.1.4 on 2020-12-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DRF', '0002_auto_20201206_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_name',
            field=models.CharField(default='null', editable=False, max_length=250),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]