from django.shortcuts import render ,redirect
from .models import*
from .forms import *
import requests
def geet_city(request):
    print('click :',request.method)
    allinfo=City.objects.all()
    if request.method=='POST':
        form=FormCity(request.POST)
        if form.is_valid():
            form.save()
            dat=form.cleaned_data.get('name')
            collecttemp=[]
            try:
                url='https://api.weatherbit.io/v2.0/forecast/daily?city={},{}&key=f2b9316a8ae248328ea4e0f005ea9e75'
                newData=requests.get(url.format(dat,'IQ')).json()
                x=newData['data']
                for i in range(len(x)):
                    collecttemp.append(x[i])
                    if len(collecttemp)>6:
                        break
            except:
                collecttemp.append('soory this city not avalible')
                return render(request,'erorr.html')
            for i in collecttemp :
                print(dat,i)
    else:
        form=FormCity()
        collecttemp=[]
        dat=''
    #citys=City.objects.all()

    allCityes=City.objects.all()
    for i in allCityes :
        print (i.id)
        if i.id>1:
            allcite=City.objects.get(pk=i.id)
            allcite.delete()
    context={'form':form ,'collecttemp':collecttemp,'dat':dat,'allinfo':allinfo,'allCityes':allCityes}
    return render(request,'wather.html',context)
# Create your views here.
