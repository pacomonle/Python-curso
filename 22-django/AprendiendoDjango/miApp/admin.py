from django.contrib import admin
# para trabajar con el admin panel importar los models de tu app en el fichero admin.py
from .models import Article, Category  # tambien se pueden importar todos *


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at') # campos de solo lectura
    pass

    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

