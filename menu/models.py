from django.db import models

class Header(models.Model):
    title = models.CharField(verbose_name="Заголовок сайта", max_length=200)
    background = models.ImageField(verbose_name="Фоновое изображение сайта", upload_to='img/dishes')
    top_pic = models.ImageField(verbose_name="Фоновое изображение кнопки АКЦИЯ", upload_to='img/dishes')



    class Meta:
        verbose_name = 'Элементы страницы'
        verbose_name_plural = 'Элементы страницы'

    def __str__(self):
        return str(self.title)

class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название раздела меню', max_length=255, unique=True)
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name


class Dishes(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда')
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)')

    class Meta:
        verbose_name = 'Блюдо стартовой страницы'
        verbose_name_plural = 'Блюда стартовой страницы'

    def __str__(self):
        return str(self.title)


class Dishes1(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда')
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)')

    class Meta:
        verbose_name = 'Блюдо страницы 1'
        verbose_name_plural = 'Блюда страницы 1'

    def __str__(self):
        return str(self.title)

class Dishes2(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда')
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)')

    class Meta:
        verbose_name = 'Блюдо страницы 2'
        verbose_name_plural = 'Блюда страницы 2'

    def __str__(self):
        return str(self.title)


class Dishes3(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда')
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)')
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)')

    class Meta:
        verbose_name = 'Блюдо страницы 3'
        verbose_name_plural = 'Блюда страницы 3'

    def __str__(self):
        return str(self.title)
