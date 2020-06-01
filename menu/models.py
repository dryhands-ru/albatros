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
    name = models.CharField(verbose_name='Название раздела вертикального меню', max_length=255, unique=True)
    class Meta:
        verbose_name = 'Пункт вертикального меню'
        verbose_name_plural = 'Пункты вертикального меню'

    def __str__(self):
        return self.name

class MenuItemHorizont(models.Model):
    name = models.CharField(verbose_name='Название раздела горизонтального меню', max_length=255, unique=True)
    class Meta:
        verbose_name = 'Пункт горизонтального меню'
        verbose_name_plural = 'Пункты горизонтального меню'

    def __str__(self):
        return self.name


class Dishes(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы АКЦИИ'
        verbose_name_plural = 'Блюда страницы АКЦИИ'

    def __str__(self):
        return str(self.title)


class Dishes1(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Холодные закуски)'
        verbose_name_plural = 'Блюда страницы (Холодные закуски)'

    def __str__(self):
        return str(self.title)

class Dishes2(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Салаты)'
        verbose_name_plural = 'Блюда страницы (Салаты)'

    def __str__(self):
        return str(self.title)


class Dishes3(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 3'
        verbose_name_plural = 'Блюда страницы 3'

    def __str__(self):
        return str(self.title)


class Dishes4(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 4'
        verbose_name_plural = 'Блюда страницы 4'

    def __str__(self):
        return str(self.title)

class Dishes5(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 5'
        verbose_name_plural = 'Блюда страницы 5'

    def __str__(self):
        return str(self.title)

class Dishes6(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 6'
        verbose_name_plural = 'Блюда страницы 6'

    def __str__(self):
        return str(self.title)

class Dishes7(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 7'
        verbose_name_plural = 'Блюда страницы 7'

    def __str__(self):
        return str(self.title)

class Dishes8(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 8'
        verbose_name_plural = 'Блюда страницы 8'

    def __str__(self):
            return str(self.title)

class Dishes100(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 100'
        verbose_name_plural = 'Блюда страницы 100'

    def __str__(self):
        return str(self.title)

class Dishes101(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 101'
        verbose_name_plural = 'Блюда страницы 101'

    def __str__(self):
        return str(self.title)

class Dishes102(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 102'
        verbose_name_plural = 'Блюда страницы 102'

    def __str__(self):
        return str(self.title)

class Dishes103(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы 103'
        verbose_name_plural = 'Блюда страницы 103'

    def __str__(self):
        return str(self.title)