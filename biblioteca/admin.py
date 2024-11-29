from django.contrib import admin
from biblioteca.models import Livro

class LivroAdmin(admin.ModelAdmin):
	list_display = ['id', 'titulo', 'autor', 'genero', 'lido', 'avaliacao']
	list_display_links = ['titulo', 'autor']
	list_per_page = 10
	search_fields = ['titulo', 'autor']
	list_filter = ['genero', 'lido', 'avaliacao']

admin.site.register(Livro, LivroAdmin)