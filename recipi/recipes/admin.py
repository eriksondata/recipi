from django.contrib import admin
from recipes.models import recipe, directions, ingredients, measurements

admin.site.register(recipe)
admin.site.register(directions)
admin.site.register(ingredients)
admin.site.register(measurements)