# Generated by Django 2.2.6 on 2019-10-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veb_site', '0009_rcomplprogects_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcomplprogects',
            name='author',
            field=models.CharField(blank=True, choices=[('admin', 'admin'), ('Test', 'Test')], db_index=True, max_length=150, null=True, verbose_name='АвторПроекта'),
        ),
    ]
