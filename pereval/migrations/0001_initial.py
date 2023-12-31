# Generated by Django 4.2.5 on 2023-12-26 21:44

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=20, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=20, verbose_name='Долгота')),
                ('height', models.IntegerField(verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название изображения')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('image', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summer', models.CharField(choices=[('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2, verbose_name='Лето')),
                ('autumn', models.CharField(choices=[('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2, verbose_name='Осень')),
                ('winter', models.CharField(choices=[('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2, verbose_name='Зима')),
                ('spring', models.CharField(choices=[('1B', '1Б'), ('2A', '2А'), ('2B', '2Б'), ('3A', '3А'), ('3B', '3Б'), ('4A', '4А'), ('4B', '4Б'), ('5A', '5А'), ('5B', '5Б'), ('6A', '6А'), ('6B', '6Б')], max_length=2, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='Perevals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=200, verbose_name='Название топонима')),
                ('title', models.CharField(max_length=200, verbose_name='Название перевала')),
                ('other_titles', models.CharField(max_length=200)),
                ('connect', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('status', models.CharField(choices=[('new', 'Создано'), ('pending', 'Взято в работу'), ('accepted', 'Успешно'), ('rejected', 'Отклонено')], default='new', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SprActivitiesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('foot', 'Пешком'), ('ski', 'Лыжи'), ('catamaran', 'Катамаран'), ('kayak', 'Байдарка'), ('raft', 'Плот'), ('alloy', 'Сплав'), ('bicycle', 'Велосипед'), ('car', 'Автомобиль'), ('sail', 'Парус'), ('horseback', 'Верхом')], max_length=10, verbose_name='Тип похода')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('otc', models.CharField(max_length=128, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(verbose_name='Телефон')),
            ],
        ),
        migrations.AddConstraint(
            model_name='users',
            constraint=models.UniqueConstraint(fields=('email',), name='user_unique'),
        ),
        migrations.AddField(
            model_name='perevals',
            name='coord',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords'),
        ),
        migrations.AddField(
            model_name='perevals',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.level'),
        ),
        migrations.AddField(
            model_name='perevals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.users'),
        ),
        migrations.AddField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pereval.perevals'),
        ),
    ]
