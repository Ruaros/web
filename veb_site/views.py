from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.views.generic import View
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'veb_site/home_page.html', context={'content_basement':take_time(), 'content': 'контент'})

def contacts(request):
    data = rContacts.objects.all() 
    context = {}
    context['content_basement'] = take_time()
    if len(data) > 0:
        objCont = data[0]        
        context['adres'] = objCont.adres
        context['telephone'] = objCont.telephone
        context['email'] = objCont.email
        context['email_href'] = 'mailto:' + objCont.email
    else:
        context['adres'] = 'Карачаево-Черкесская республика, Малокарачаевский район, с. Первомайское, д.6'
        context['telephone'] = '+7(928)337-73-37'
        context['email'] = '8175557@mail.ru'
        context['email_href'] = 'mailto:8175557@mail.ru'

    return render(request, 'veb_site/contacts.html', context)

def design(request):
    return render(request, 'veb_site/works.html', context={'content_basement':take_time(), 'design':True})

def building(request):
    return render(request, 'veb_site/works.html', context={'content_basement':take_time(), 'building':True})

def expertise(request):
    return render(request, 'veb_site/works.html', context={'content_basement':take_time(), 'expertise':True})

def services(request):
    return render(request, 'veb_site/works.html', context={'content_basement':take_time()})

def take_time():
    return str(datetime.now().year)#+ "." + str(datetime.now().month) + "." + str(datetime.now().day)

def project_page(request, article, type):

    data = rComplProgects.objects.get(article=int(article))
    context={'content_basement':take_time()}

    cards = []
    for atribute in data._meta.get_fields():
        if atribute.name != 'id':
            obj = getattr(data, atribute.name)
            if not obj:
                continue
            if atribute.name[:3] == 'img':
                if atribute.name == 'img_main':
                    context['main'] = obj.url
                    cards.append(obj.url)
                else:
                    cards.append(obj.url)
            else:
                context[data._meta.get_field(atribute.name).verbose_name] = obj
     
    context['cards'] = cards
    
    dostup = False
    if request.user.is_authenticated and request.user.is_staff:
        if request.user.is_superuser or request.user.username == data.author:
            dostup = True   
    context['dostup'] = dostup

    return render(request, 'veb_site/project_page.html', context)

def feedback(request):
    article = None
    if 'article' in request.GET:
        article = request.GET['article']
    return render(request, 'veb_site/feedback.html', context={'content_basement':take_time(), 'article':article})

def feedback_send_message(request, data):
                 
         if not (data.get('email') or data.get('tel')):
            error_message = 'Чтобы мы могли с вами связаться, необходимо ввести Email либо номер телефона.'
            return render(request, 'veb_site/feedback.html', context={'content_basement':take_time(), 'error': error_message})
         message = 'Товарищ {' + data.get('name') + "}, из организации {" + data.get('town') + "}, запрашивает следующую информацию.\n"
         message = message + '{' + data.get('comment') + '}' + '\n'
         if data.get('article'):
            message = message + 'Запрашивается проект {' + data.get('article') + '}' + '\n'
            author = rComplProgects.objects.get(article = int(data.get('article'))).author
            message = message + 'Автор проекта: ' + author + '\n'
         message = message + 'Контактные данные:\n'
         message = message + 'Телефон:' + data.get('tel') + '\n'
         message = message + 'Email:' + data.get('email') + '\n'

         #Подключение и отправка почты
         obj = rContacts.objects.all()
         if len(obj) > 0:
            remail = obj[0].email
         else:
            remail = '8175557@mail.ru'

         res = send_email(message, remail, data)
         return render(request, 'veb_site/feedback.html', context={'content_basement':take_time(), 'error': 'Ваше сообщение успешно отправлено' if res == True else 'Не удалось отправить сообщение. Для консультации, перезвоните пожалуйста по номеру +7(928)337-73-37'})

def send_email(message, remail, data):
    import smtplib
    from email.mime.text import MIMEText
    from email.header    import Header

    username = 'botprogect212'
    password = 'qwertybotprogect212'
    smtp_server = 'smtp.yandex.ru'
    port = 587

    msg = MIMEText(message, 'plain', 'utf-8')
    msg['Subject'] = Header('Потенциальный клиент', 'utf-8')
    msg['From'] = Header("Клиент <botprogect212@yandex.ru>", 'utf-8')
    msg['To'] = Header("Хозяин <" + remail + ">", 'utf-8')
  
    try:
        obj = rWantContacts.objects.create(name=data.get('name'),
                                           town=data.get('town'),
                                           email=data.get('email'),
                                           tel=data.get('tel'),
                                           article=data.get('article'),
                                           comment=data.get('comment')
                                           )
        server = smtplib.SMTP(smtp_server, port, timeout=15)
        server.starttls()
        server.login(username, password)
        server.sendmail('botprogect212@yandex.ru', remail, msg.as_string())
        server.quit()
        obj.success = True
        obj.save()
        return True
    except:
        return False

def done_projects(request):
    data = rComplProgects.objects.filter(typing='done_projects')
    return render(request, 'veb_site/done_projects.html', context={'content_basement':take_time(), 'content': data})
    

def make_values():
    values = {
                    'Цена':{'min_price':None, 'max_price':None},
                    'Общая площадь':{'min_all_square':None, 'max_all_square':None},
                    'Жилая площадь':{'min_live_square':None, 'max_live_square':None},
                    'Кол-во этажей':{'min_floor':None, 'max_floor':None},
                    'Кол-во спален':{'min_bedrooms':None, 'max_bedrooms':None},
                    'Кол-во сан. узлов':{'min_bahtrooms':None, 'max_bahtrooms':None},                
                    } 
    return values

def filtrate(request, type):
    if 'Cancel' in request.GET:
        data = rComplProgects.objects.filter(typing=type)
        return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':type, 'values':make_values()})
    else:
        fil = make_filters(request.GET)
        filters = fil[0]
        
        data = rComplProgects.objects.filter(typing=type, 
                                         price__range = filters['price'],
                                         all_square__range = filters['all_square'],
                                         live_square__range = filters['live_square'],
                                         floor__range = filters['floor'],
                                         bedrooms__range = filters['bedrooms'],
                                         bahtrooms__range = filters['bahtrooms']
                                         )
        return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':type, 'values':fil[1]})

def make_filters(GET):
    filters = {
              'price':[0,999999],
              'floor':[0,9],
              'bedrooms':[0,9],
              'bahtrooms':[0,9],
              'all_square':[0,999],
              'live_square':[0,999],              
             }  
    
    values = make_values()

    for filter in filters:
        for prefix in ['min_', 'max_']:
            prefix_filter= prefix + filter
            if prefix_filter in GET:                
                obj = GET[prefix_filter]
                if obj != '': 
                    filters[filter][0 if prefix == 'min_' else 1] = int(obj)
                    #Пока так
                    for x in values:
                        for y in values[x]:
                            if y==prefix_filter:
                                values[x][prefix_filter] = int(obj)

                    
    return filters, values

def houses(request):  
    data = rComplProgects.objects.filter(typing='houses')
    return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':'houses', 'values':make_values()})

def complexes(request):
    data = rComplProgects.objects.filter(typing='complexes')
    return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':'complexes', 'values':make_values()})

def hotels(request):
    data = rComplProgects.objects.filter(typing='hotels')
    return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':'hotels', 'values':make_values()})

def ets(request):
    data = rComplProgects.objects.filter(typing='ets')
    return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data, 'ВидПроекта':'ets', 'values':make_values()})

class project_create(View):
    
    def get(self, request):
        form = rComplProgectsForm(initial={'author': request.user.username})
        return render(request, 'veb_site/create_project.html', context={'content_basement':take_time(),'form':form})
 
    def post(self, request):
        bound_form = rComplProgectsForm(request.POST, request.FILES) 
        
        if bound_form.is_valid():
            new_project = bound_form.save()
            #return project_page(request, new_project.article, new_project.typing)
            return redirect(new_project)  
        
        return render(request, 'veb_site/create_project.html', context={'form':bound_form})
    
class make_Contact(View):

    def get(self, request):
        article = request.GET['article'] if 'article' in request.GET else None
        form = ContactForm(initial={'article': article})
        return render(request, 'veb_site/feedback.html', context={'content_basement':take_time(), 
                                                                  'form':form, 
                                                                  'article':article})
 
    def post(self, request):
        bound_form = ContactForm(request.POST) 
        
        if bound_form.is_valid():
            return feedback_send_message(request, bound_form.cleaned_data)   
        
        return render(request, 'veb_site/feedback.html', context={'content_basement':take_time(), 'form':bound_form})    

class project_update(View):

    def get(self, request, article, type):
        project = rComplProgects.objects.get(article=int(article))
        bound_form = rComplProgectsForm(instance=project)
        return render(request, 'veb_site/project_update.html', context={'form':bound_form, 'content_basement':take_time()})

    def post(self, request, article, type):
        project = rComplProgects.objects.get(article=int(article))
        bound_form = rComplProgectsForm(request.POST, request.FILES, instance=project)
        if bound_form.is_valid():
            new_project = bound_form.save()
            #return feedback_send_message(request, bound_form.cleaned_data)
            return redirect(new_project)        
        return render(request, 'veb_site/project_update.html', context={'content_basement':take_time(),'form':bound_form})

class project_delete(View):
    def get(self, request, article, type):
        project = rComplProgects.objects.get(article=int(article))
        project.delete()
        data = rComplProgects.objects.filter(typing=type)
        return render(request, 'veb_site/complete_projects.html', context={'content_basement':take_time(), 'content': data})
