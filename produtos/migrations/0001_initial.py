# Generated by Django 4.1 on 2022-12-07 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MiniCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('data_nascimento', models.DateTimeField()),
                ('senha', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço do produto')),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, max_length=250, null=True, upload_to='produto/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.categoria')),
            ],
        ),
    ]