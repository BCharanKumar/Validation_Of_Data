from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_student(request):
    ESMFO=StudentModelForm()
    d={'ESMFO':ESMFO}
    if request.method=='POST':
        SMFDO=StudentModelForm(request.POST)
        if SMFDO.is_valid():
            SMFDO.save()
            #return HttpResponse('data insert succesfully')
            return HttpResponse(str(SMFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_student.html',d)