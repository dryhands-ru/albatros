# Generated by Django 3.0.6 on 2020-05-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_photo', models.ImageField(upload_to='img/dishes', verbose_name='Фото блюда')),
                ('text', models.TextField(verbose_name='Описание блюда')),
                ('price', models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')),
                ('weight', models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)')),
            ],
            options={
                'verbose_name': 'Блюдо стартовой страницы',
                'verbose_name_plural': 'Блюда стартовой страницы',
            },
        ),
        migrations.AlterModelOptions(
            name='dishes',
            options={'verbose_name': 'Блюдо стартовой страницы', 'verbose_name_plural': 'Блюда стартовой страницы'},
        ),
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)'),
        ),
        migrations.AlterField(
            model_name='dishes',
            name='weight',
            field=models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)'),
        ),
    ]
