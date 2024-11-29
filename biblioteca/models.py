from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Livro(models.Model):

	GENEROS = (
		('NF', 'NÃO_FICÇÃO'),
		('F', 'FICÇÃO'),
		)

	titulo = models.CharField(max_length=100, null=False, blank=False, unique=True)
	autor = models.CharField(max_length=50)
	genero = models.CharField(max_length=2, choices=GENEROS, default='NF')
	lido = models.BooleanField(default=False)
	avaliacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)

	def __str__(self):
		return self.titulo
