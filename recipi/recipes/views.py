# Create your views here.
from django.template import Context, Template
from django.template.loader import 

from recipes.models import recipe, directions, ingredients, measurements

def showIndex(request):
    pass