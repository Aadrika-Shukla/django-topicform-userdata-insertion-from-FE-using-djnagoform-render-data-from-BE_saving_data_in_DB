from django.shortcuts import render

from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.


#for collecting the recieved form data

def insert_topic(request):
    ETFO=TopicForm()                             #EMPTY TOPIC FORM OBJECT TO DISPLAY INPUT ELEMENTS
    d={'ETFO':ETFO}            
    if request.method=='POST':
        TDFO=TopicForm(request.POST)             #TO COLLECT THE DATA WHERE DATA IS IN request.POST and our wrapper in form object that is TopicForm
        if TDFO.is_valid():                      #to validate the data
            #print(TDFO.cleaned_data)
            TO=TDFO.cleaned_data['topic_name']     #to collect the validated data recieved from form by user
            #print(TO)
            TTDO=Topic.objects.get_or_create(topic_name=TO)[0]#to insert that collected data into our databse /model/table from be
            TTDO.save()
           
            return HttpResponse('Topic inserted successfully into my database')
            
            
        else:
            return HttpResponse('invalid topic name insertion')
        
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO= Webpageform()                             #EMPTY WEBPAGE FORM OBJECT TO DISPLAY INPUT ELEMENTS
    d={'EWFO':EWFO}            
    if request.method=='POST':
        WDFO=Webpageform(request.POST)             #TO COLLECT THE DATA WHERE DATA IS IN request.POST and our wrapper in form object that is WebpageForm
        if WDFO.is_valid():                      #to validate the data
            #print(TDFO.cleaned_data)
            TTO=WDFO.cleaned_data['topic_name']#to collect the validated data recieved from form by user
            wname=WDFO.cleaned_data['name']
            wurl=WDFO.cleaned_data['url']
            wemail=WDFO.cleaned_data['email']
            #print(TO)
            TO=Topic.objects.get(topic_name=TTO)      #where ,topic_name,name,url,email are the column names given in my models.py file for respective tables
            WTDO=WebPage.objects.get_or_create(topic_name=TO,name=wname,url=wurl,email=wemail)[0]   #to insert that collected data into our databse /model/table from be
            WTDO.save()
            #print(WTDO)
            return HttpResponse('Webpage inserted successfully into my database')
            
            
        else:
            return HttpResponse('invalid webpage data insertion')
        
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    EAFO= Accessform()                             #EMPTY WEBPAGE FORM OBJECT TO DISPLAY INPUT ELEMENTS
    d={'EAFO':EAFO}            
    if request.method=='POST':
        ADFO=Accessform(request.POST)             #TO COLLECT THE DATA WHERE DATA IS IN request.POST and our wrapper in form object that is WebpageForm
        if ADFO.is_valid():                      #to validate the data
            #print(TDFO.cleaned_data)
            WNO=ADFO.cleaned_data['name']#to collect the validated data recieved from form by user
            adate=ADFO.cleaned_data['date']
            aauth=ADFO.cleaned_data['author']
            #print(TO)
            WO=WebPage.objects.get(name=WNO)         #where name,date,author are the column names given in my models.py file for respective tables
            ATDO=AccessRecord.objects.get_or_create(name=WO,date=adate,author=aauth)[0]   #to insert that collected data into our databse /model/table from be
            ATDO.save()
            #print(WTDO)
            return HttpResponse('Access Record inserted successfully into my database')
            
            
        else:
            return HttpResponse('invalid  data insertion for Access records')
        
    return render(request,'insert_access.html',d)

