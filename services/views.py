from django.shortcuts import render
from .models import Equip

# Create your views here.
def services(request):
    allinfo=Equip.objects.all()
    context1 = {'allinfokey': allinfo}
    return render(request,"services.html",context1)