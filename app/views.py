from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def create_company(request):
    ECFO=CompanyForm()
    d={'ECFO':ECFO}
    if request.method=='POST':
        CFDO=CompanyForm(request.POST)
        if CFDO.is_valid():
            cn=CFDO.cleaned_data['cname']
            cm=CFDO.cleaned_data['cmanager']
            cl=CFDO.cleaned_data['clocation']
            CO=Company.objects.get_or_create(cname=cn,cmanager=cm,clocation=cl)[0]
            CO.save()
            return HttpResponse('company is created')
        else:
            return HttpResponse('data is invalid')
    return render(request,'create_company.html',d)
   
    


    
    