from django import forms
from .models import rComplProgects 

class rComplProgectsForm(forms.ModelForm):

    class Meta:
        model = rComplProgects
        fields=[
            'title',
            'img_main',
            'img_1',
            'img_2',
            'img_3',
            'img_4',
            'img_5',
            'img_6',
            'img_7',
            'img_8',
            'img_9',
            'img_10',
            'description',
            'typing',
            'price',            
            'all_square',
            'live_square',
            'roof_square',
            'height',
            'height_ceiling',
            'angle_roof',
            'floor',
            'bedrooms',
            'bahtrooms',
            'garage',
            'coob',
            'min_width',
            'min_length',
            'walls',
            'overlap',
            'housetop',
            'foundation',
            'author',
                ]

        labels = {
            'title':'Заголовок',
            'img_main':'Заставка',
            'img_1':'img 1',
            'img_2':'img 2',
            'img_3':'img 3',
            'img_4':'img 4',
            'img_5':'img 5',
            'img_6':'img 6',
            'img_7':'img 7',
            'img_8':'img 8',
            'img_9':'img 9',
            'img_10':'img 10',
            'description':'Описание',
            'typing':'Вид проекта',
            'price':'Цена',
            'all_square':'Общая площадь',
            'live_square':'Жилая площадь',
            'roof_square':'Площадь крыши',
            'height':'Высота здания',
            'height_ceiling':'Высота потолка',
            'angle_roof':'Угол наклона кровли',
            'floor':'Этажность',
            'bedrooms':'Количество спален',
            'bahtrooms':'Количество санузлов',
            'garage':'Наличие гаража',
            'coob':'Кубатура',
            'min_width':'Минимальный размер участка (ширина)',
            'min_length':'Минимальный размер участка (длина)',
            'walls':'Стены',
            'overlap':'Перекрытие',
            'housetop':'Кровля',
            'foundation':'Фундамент',
            'author':'Автор',
        }

        widget = {
            'title':forms.TextInput(attrs={'class':"form-control"}),
            'img_main':forms.TextInput(attrs={'class':"form-control"}),
            'img_1':forms.TextInput(attrs={'class':"form-control"}),
            'img_2':forms.TextInput(attrs={'class':"form-control"}),
            'img_3':forms.TextInput(attrs={'class':"form-control"}),
            'img_4':forms.TextInput(attrs={'class':"form-control"}),
            'img_5':forms.TextInput(attrs={'class':"form-control"}),
            'img_6':forms.TextInput(attrs={'class':"form-control"}),
            'img_7':forms.TextInput(attrs={'class':"form-control"}),
            'img_8':forms.TextInput(attrs={'class':"form-control"}),
            'img_9':forms.TextInput(attrs={'class':"form-control"}),
            'img_10':forms.TextInput(attrs={'class':"form-control"}),
            'description':forms.TextInput(attrs={'class':"form-control"}),
            'typing':forms.TextInput(attrs={'class':"form-control"}),
            'price':forms.TextInput(attrs={'class':"form-control"}),
            'all_square':forms.TextInput(attrs={'class':"form-control"}),
            'live_square':forms.TextInput(attrs={'class':"form-control"}),
            'roof_square':forms.TextInput(attrs={'class':"form-control"}),
            'height':forms.TextInput(attrs={'class':"form-control"}),
            'height_ceiling':forms.TextInput(attrs={'class':"form-control"}),
            'angle_roof':forms.TextInput(attrs={'class':"form-control"}),
            'floor':forms.TextInput(attrs={'class':"form-control"}),
            'bedrooms':forms.TextInput(attrs={'class':"form-control"}),
            'bahtrooms':forms.TextInput(attrs={'class':"form-control"}),
            'garage':forms.TextInput(attrs={'class':"form-control"}),
            'coob':forms.TextInput(attrs={'class':"form-control"}),
            'min_width':forms.TextInput(attrs={'class':"form-control"}),
            'min_length':forms.TextInput(attrs={'class':"form-control"}),
            'walls':forms.TextInput(attrs={'class':"form-control"}),
            'overlap':forms.TextInput(attrs={'class':"form-control"}),
            'housetop':forms.TextInput(attrs={'class':"form-control"}),
            'foundation':forms.TextInput(attrs={'class':"form-control"}),
            'author':forms.TextInput(attrs={'class':"form-control"}),
            }
    

    #def save(self):
    #    f = []
    #    for x in rComplProgects.objects.all():
    #        f.append(x.article)
    #    max_article = 1030299 if len(f)==0 else max(f)
    #
    #    new_progects = rComplProgects.objects.create(
    #                    title    = self.cleaned_data.get('title'),
    #                    article  = max_article+1,
    #                    img_main = self.cleaned_data.get('img_main'),
    #                    img_1    = self.cleaned_data.get('img_1'),
    #                    img_2    = self.cleaned_data.get('img_2'),
    #                    img_3    = self.cleaned_data.get('img_3'),
    #                    img_4    = self.cleaned_data.get('img_4'),
    #                    img_5    = self.cleaned_data.get('img_5'),
    #                    img_6    = self.cleaned_data.get('img_6'),
    #                    img_7    = self.cleaned_data.get('img_7'),
    #                    img_8    = self.cleaned_data.get('img_8'),
    #                    img_9    = self.cleaned_data.get('img_9'),
    #                    img_10    = self.cleaned_data.get('img_10'),
    #                    description = self.cleaned_data.get('description'),
    #                    typing      = self.cleaned_data.get('typing'),
    #                    price       = self.cleaned_data.get('price'),
    #                    all_square  = self.cleaned_data.get('all_square'),
    #                    live_square = self.cleaned_data.get('live_square'),
    #                    roof_square = self.cleaned_data.get('roof_square'),
    #                    height      = self.cleaned_data.get('height'),
    #                    height_ceiling  = self.cleaned_data.get('height_ceiling'),
    #                    angle_roof      = self.cleaned_data.get('angle_roof'),
    #                    floor           = self.cleaned_data.get('floor'),
    #                    bedrooms        = self.cleaned_data.get('bedrooms'),
    #                    bahtrooms       = self.cleaned_data.get('bahtrooms'),
    #                    garage          = self.cleaned_data.get('garage'),
    #                    coob            = self.cleaned_data.get('coob'),
    #                    min_width       = self.cleaned_data.get('min_width'),
    #                    min_length      = self.cleaned_data.get('min_length'),
    #                    walls           = self.cleaned_data.get('walls'),
    #                    overlap         = self.cleaned_data.get('overlap'),
    #                    housetop        = self.cleaned_data.get('housetop'),
    #                    foundation      = self.cleaned_data.get('foundation')
    #                                 
    #        )
    #    return new_progects

class ContactForm(forms.Form):
    name = forms.CharField(label=u'Ваше имя, должность', max_length=150, required=False)
    town = forms.CharField(label=u'Название предприятия, город', max_length=150, required=False)
    tel = forms.CharField(label=u'Контактный телефон *', max_length=150, required=True)
    email = forms.EmailField(label=u'Электронная почта *', max_length=150, required=True)
    article = forms.CharField(label=u'Артикул проекта', max_length=150, required=False)
    comment = forms.CharField(label=u'Комментарий', max_length=150, required=False)

    name.widget.attrs.update({'class':"form-control"})
    town.widget.attrs.update({'class':"form-control"})
    tel.widget.attrs.update({'class':"form-control"})
    email.widget.attrs.update({'class':"form-control"})
    article.widget.attrs.update({'class':"form-control"})
    comment.widget.attrs.update({'class':"form-control"})
 