# Generated by Django 2.2.6 on 2019-10-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rComplProgects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('article', models.IntegerField(default=0, unique=True, verbose_name='Артикль')),
                ('datatime', models.DateTimeField(auto_now_add=True, verbose_name='ВремяДобавления')),
                ('img_main', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Заставка')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_1')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_2')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_3')),
                ('img_4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_4')),
                ('img_5', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_5')),
                ('img_6', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_6')),
                ('img_7', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изо_7')),
                ('description', models.TextField(default='', max_length=400, null=True, verbose_name='Описание')),
                ('typing', models.CharField(db_index=True, default='house', max_length=150, null=True, verbose_name='ВидПроекта')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Цена')),
                ('all_square', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='ОбщаяПлощадь')),
                ('live_square', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='ЖилаяПлощадь')),
                ('roof_square', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='ПлощадьКрыши')),
                ('height', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='ВысотаЗдания')),
                ('height_ceiling', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='ВысотаПотолка')),
                ('angle_roof', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='УголНаклонаКровли')),
                ('floor', models.IntegerField(default=1, null=True, verbose_name='Этажность')),
                ('bedrooms', models.IntegerField(default=0, null=True, verbose_name='КоличествоСпален')),
                ('bahtrooms', models.IntegerField(default=0, null=True, verbose_name='КоличествоСанузлов')),
                ('garage', models.TextField(default='Нет', max_length=3, null=True, verbose_name='НаличиеГаража')),
                ('coob', models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True, verbose_name='Кубатура')),
                ('min_width', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='МинимальныйРазмерУчастка_ширина')),
                ('min_length', models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='МинимальныйРазмерУчастка_длина')),
                ('walls', models.TextField(default='', max_length=150, null=True, verbose_name='Стены')),
                ('overlap', models.TextField(default='', max_length=150, null=True, verbose_name='Перекрытие')),
                ('housetop', models.TextField(default='', max_length=150, null=True, verbose_name='Кровля')),
                ('foundation', models.TextField(default='', max_length=150, null=True, verbose_name='Фундамент')),
            ],
        ),
    ]
