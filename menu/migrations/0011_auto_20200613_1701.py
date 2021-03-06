# Generated by Django 3.0.6 on 2020-06-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20200608_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes14',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(blank=True, verbose_name='Описание блюда')),
                ('price', models.CharField(blank=True, default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(blank=True, default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы (Соус)',
                'verbose_name_plural': 'Блюда страницы (Соус)',
            },
        ),
        migrations.CreateModel(
            name='Dishes15',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(blank=True, verbose_name='Описание блюда')),
                ('price', models.CharField(blank=True, default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(blank=True, default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы (Соус)',
                'verbose_name_plural': 'Блюда страницы (Соус)',
            },
        ),
        migrations.CreateModel(
            name='Dishes16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(blank=True, verbose_name='Описание блюда')),
                ('price', models.CharField(blank=True, default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(blank=True, default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы (Соус)',
                'verbose_name_plural': 'Блюда страницы (Соус)',
            },
        ),
        migrations.CreateModel(
            name='Dishes9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(blank=True, verbose_name='Описание блюда')),
                ('price', models.CharField(blank=True, default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(blank=True, default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо страницы (Гарниры)',
                'verbose_name_plural': 'Блюда страницы (Гарниры)',
            },
        ),
        migrations.RenameModel(
            old_name='Dishes102',
            new_name='Dishes10',
        ),
        migrations.RenameModel(
            old_name='Dishes103',
            new_name='Dishes11',
        ),
        migrations.RenameModel(
            old_name='Dishes100',
            new_name='Dishes12',
        ),
        migrations.RenameModel(
            old_name='Dishes101',
            new_name='Dishes13',
        ),
        migrations.AlterModelOptions(
            name='dishes10',
            options={'verbose_name': 'Блюдо страницы (Блюда на мангале)', 'verbose_name_plural': 'Блюда страницы (Блюда на мангале)'},
        ),
        migrations.AlterModelOptions(
            name='dishes11',
            options={'verbose_name': 'Блюдо страницы (Овощи на мангале)', 'verbose_name_plural': 'Блюда страницы (Овощи на мангале)'},
        ),
        migrations.AlterModelOptions(
            name='dishes12',
            options={'verbose_name': 'Блюдо страницы (Соус)', 'verbose_name_plural': 'Блюда страницы (Соус)'},
        ),
        migrations.AlterModelOptions(
            name='dishes13',
            options={'verbose_name': 'Блюдо страницы (Соус)', 'verbose_name_plural': 'Блюда страницы (Соус)'},
        ),
        migrations.AlterModelOptions(
            name='dishes3',
            options={'verbose_name': 'Блюдо страницы (Горячие закуски)', 'verbose_name_plural': 'Блюда страницы (Горячие закуски)'},
        ),
        migrations.AlterModelOptions(
            name='dishes4',
            options={'verbose_name': 'Блюдо страницы (Первые блюда)', 'verbose_name_plural': 'Блюда страницы (Первые блюда)'},
        ),
        migrations.AlterModelOptions(
            name='dishes5',
            options={'verbose_name': 'Блюдо страницы (Горячие блюда из рыбы и морепродуктов)', 'verbose_name_plural': 'Блюда страницы (Горячие блюда из рыбы и морепродуктов)'},
        ),
        migrations.AlterModelOptions(
            name='dishes6',
            options={'verbose_name': 'Блюдо страницы (Горячие блюда из мяса)', 'verbose_name_plural': 'Блюда страницы (Горячие блюда из мяса)'},
        ),
        migrations.AlterModelOptions(
            name='dishes7',
            options={'verbose_name': 'Блюдо страницы (Стейк меню)', 'verbose_name_plural': 'Блюда страницы (Стейк меню)'},
        ),
        migrations.AlterModelOptions(
            name='dishes8',
            options={'verbose_name': 'Блюдо страницы (Су вид меню)', 'verbose_name_plural': 'Блюда страницы (Су вид меню)'},
        ),
    ]
