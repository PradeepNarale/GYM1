from django.shortcuts import render
from .models import Product
# Create your views here.
def product(request):
    all_info = Product.objects.all()
    context = {'all_info_key': all_info}
    return render(request,"product.html",context)





