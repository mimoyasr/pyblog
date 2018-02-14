from django.shortcuts import render
from .models import Category

def allcategories(request):
    all_categories=Category.objects.all()
    context={"allcategories":all_categories}
    return render(request,"",context)
