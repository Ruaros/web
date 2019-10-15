# Generated by Django 2.2.6 on 2019-10-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veb_site', '0015_auto_20191014_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='rWantContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя, должность')),
                ('town', models.CharField(max_length=150, verbose_name='Организация, город')),
                ('tel', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('article', models.CharField(max_length=150, verbose_name='Артикул')),
                ('comment', models.CharField(max_length=150, verbose_name='Комментарий')),
                ('success', models.BooleanField(default=False, verbose_name='Письмо отправлено')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]