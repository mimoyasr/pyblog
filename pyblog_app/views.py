from django.core import serializers
from django.http import JsonResponse
from .models import Category


def allcategories(request):
    all_categories = Category.objects.all()
    return JsonResponse(serializers.serialize('json', all_categories), safe=False)
