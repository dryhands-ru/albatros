# Generated by Django 3.0.6 on 2020-06-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20200601_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes100',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 100',
                'verbose_name_plural': 'Блюда страницы 100',
            },
        ),
        migrations.CreateModel(
            name='Dishes101',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 101',
                'verbose_name_plural': 'Блюда страницы 101',
            },
        ),
        migrations.CreateModel(
            name='Dishes102',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 102',
                'verbose_name_plural': 'Блюда страницы 102',
            },
        ),
        migrations.CreateModel(
            name='Dishes103',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 103',
                'verbose_name_plural': 'Блюда страницы 103',
            },
        ),
        migrations.CreateModel(
            name='Dishes5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 5',
                'verbose_name_plural': 'Блюда страницы 5',
            },
        ),
        migrations.CreateModel(
            name='Dishes6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 6',
                'verbose_name_plural': 'Блюда страницы 6',
            },
        ),
        migrations.CreateModel(
            name='Dishes7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 7',
                'verbose_name_plural': 'Блюда страницы 7',
            },
        ),
        migrations.CreateModel(
            name='Dishes8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы 8',
                'verbose_name_plural': 'Блюда страницы 8',
            },
        ),
    ]
