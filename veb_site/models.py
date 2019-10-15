from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .utils import get_path

# Create your models here.
def gen_article():
    f = []
    for x in rComplProgects.objects.all():
        f.append(x.article)
    return 1030299 if len(f)==0 else max(f)+1

class rComplProgects(models.Model):
    title    = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок')
    article  = models.IntegerField(default=0, unique=True, verbose_name='Артикль')
    datatime = models.DateTimeField(auto_now_add=True, verbose_name='ВремяДобавления')
    img_main = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Заставка')
    img_1    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_1')
    img_2    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_2')
    img_3    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_3')
    img_4    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_4')
    img_5    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_5')
    img_6    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_6')
    img_7    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_7')
    img_8    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_8')
    img_9    = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_9')
    img_10   = models.ImageField(upload_to=get_path, null=True, blank=True, verbose_name='Изо_10')
    description = models.TextField(max_length=400, default='', null=True, blank=True, verbose_name='Описание')
    type_choicis = (
        ('houses',        'Дома'),
        ("hotels",        "Отели"),
        ("complexes",     "Жив. комплексы"),
        ("ets",           "Мойки, заправки и т.д."),
        ("done_projects", "Готовые проекты"),
    )
    typing      = models.CharField(max_length=150, choices=type_choicis, default='houses', null=True, db_index=True, verbose_name='ВидПроекта')    
    price          = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name='Цена')    
    all_square     = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='ОбщаяПлощадь')
    live_square    = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='ЖилаяПлощадь')
    roof_square    = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='ПлощадьКрыши')
    height         = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='ВысотаЗдания')
    height_ceiling = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='ВысотаПотолка')
    angle_roof     = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='УголНаклонаКровли')
    int_choicis = (
        (0, '0'),
        (1, '1'),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        )
    floor          = models.IntegerField(default=1, choices=int_choicis, null=True, blank=True, verbose_name='Этажность')
    bedrooms       = models.IntegerField(default=0, choices=int_choicis, null=True, blank=True, verbose_name='КоличествоСпален')
    bahtrooms      = models.IntegerField(default=0, choices=int_choicis, null=True, blank=True, verbose_name='КоличествоСанузлов')
    yes_no_choicis = (
         ("Нет", "Нет"),
         ('Да', 'Да'),
        )
    garage         = models.TextField(max_length=3, choices=yes_no_choicis, default='Нет', null=True, blank=True, verbose_name='НаличиеГаража')
    coob           = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True, verbose_name='Кубатура')
    min_width      = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='МинимальныйРазмерУчастка_ширина') 
    min_length     = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=True, blank=True, verbose_name='МинимальныйРазмерУчастка_длина')
    walls          = models.TextField(max_length=150, default='', null=True, blank=True, verbose_name='Стены')
    overlap        = models.TextField(max_length=150, default='', null=True, blank=True, verbose_name='Перекрытие')
    housetop       = models.TextField(max_length=150, default='', null=True, blank=True, verbose_name='Кровля')
    foundation     = models.TextField(max_length=150, default='', null=True, blank=True, verbose_name='Фундамент')

    authors = []
    for user_ in User.objects.all():
        authors.append((user_.username, user_.username))
    author_choicis = (authors)

    author         = models.CharField(max_length=150, choices=author_choicis, null=True, blank=True, db_index=True, verbose_name='АвторПроекта')    


    def get_absolute_url(self):
        return reverse('project_page_url', kwargs={'article':self.article, 'type':self.typing})

    def save(self, *args, **kwargs):
        if not self.id:
            self.article = gen_article()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class rContacts(models.Model):
    adres = models.CharField(max_length=150, verbose_name='Адрес')
    email = models.CharField(max_length=150, verbose_name='Электронная почта')
    telephone = models.CharField(max_length=150, verbose_name='Номер телефона')
        
    class Meta:
        verbose_name = "Контактные данные"
        verbose_name_plural = "Контактные данные"

class rWantContacts(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя, должность')
    town = models.CharField(max_length=150, verbose_name='Организация, город')
    tel = models.CharField(max_length=150, verbose_name='Номер телефона')
    email = models.EmailField(max_length=150, verbose_name='Email')
    article = models.CharField(max_length=150, verbose_name='Артикул')
    comment = models.CharField(max_length=150, verbose_name='Комментарий')
    success = models.BooleanField(default=False,  verbose_name='Письмо отправлено')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"