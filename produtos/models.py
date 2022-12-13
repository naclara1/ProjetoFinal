from django.db import models

class Categoria(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField('Preço do produto', max_digits=8, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produto/', blank=True, null=True, max_length=250)


LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

LISTA_CURSO= [
    ('ADS', 'ADS'),
    ('Agronomia', 'Agronomia'),
    ('Química', 'Química'),
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    data_nascimento = models.DateTimeField()
    senha = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome