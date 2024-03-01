from django.shortcuts import render
from .models import travel

# Create your views here.
def link1(request):
    dest = travel.objects.all()
    return render(request,'index.html',{'dest':dest})
