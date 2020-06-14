from django.db import models


class Header(models.Model):
    title = models.CharField(verbose_name="Заголовок сайта", max_length=200)
    backgroundMain = models.ImageField(default='', verbose_name="Фоновое изображение стартовой страницы сайта", upload_to='img/dishes')
    background = models.ImageField(verbose_name="Фоновое изображение сайта", upload_to='img/dishes')
    top_pic = models.ImageField(verbose_name="Фоновое изображение кнопки АКЦИЯ", upload_to='img/dishes')

    class Meta:
        verbose_name = 'Элементы страницы'
        verbose_name_plural = 'Элементы страницы'

    def __str__(self):
        return str(self.title)


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название раздела меню', max_length=255, unique=True)
    image = models.ImageField(default='', verbose_name="Фоновое изображение раздела меню", upload_to='img/dishes')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

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
        verbose_name = 'Блюдо страницы (Горячие закуски)'
        verbose_name_plural = 'Блюда страницы (Горячие закуски)'

    def __str__(self):
        return str(self.title)


class Dishes4(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0',max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Первые блюда)'
        verbose_name_plural = 'Блюда страницы (Первые блюда)'

    def __str__(self):
        return str(self.title)


class Dishes5(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Горячие блюда из рыбы и морепродуктов)'
        verbose_name_plural = 'Блюда страницы (Горячие блюда из рыбы и морепродуктов)'

    def __str__(self):
        return str(self.title)


class Dishes6(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Горячие блюда из мяса)'
        verbose_name_plural = 'Блюда страницы (Горячие блюда из мяса)'

    def __str__(self):
        return str(self.title)


class Dishes7(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Стейк меню)'
        verbose_name_plural = 'Блюда страницы (Стейк меню)'

    def __str__(self):
        return str(self.title)


class Dishes8(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Су вид меню)'
        verbose_name_plural = 'Блюда страницы (Су вид меню)'

    def __str__(self):
            return str(self.title)


class Dishes9(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Гарниры)'
        verbose_name_plural = 'Блюда страницы (Гарниры)'

    def __str__(self):
        return str(self.title)


class Dishes10(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Блюда на мангале)'
        verbose_name_plural = 'Блюда страницы (Блюда на мангале)'

    def __str__(self):
        return str(self.title)


class Dishes11(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Овощи на мангале)'
        verbose_name_plural = 'Блюда страницы (Овощи на мангале)'

    def __str__(self):
        return str(self.title)


class Dishes12(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Соус)'
        verbose_name_plural = 'Блюда страницы (Соус)'

    def __str__(self):
        return str(self.title)


class Dishes13(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Соус)'
        verbose_name_plural = 'Блюда страницы (Соус)'

    def __str__(self):
        return str(self.title)

class Dishes14(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Соус)'
        verbose_name_plural = 'Блюда страницы (Соус)'

    def __str__(self):
        return str(self.title)


class Dishes15(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Соус)'
        verbose_name_plural = 'Блюда страницы (Соус)'

    def __str__(self):
        return str(self.title)


class Dishes16(models.Model):
    title = models.CharField(max_length=200)
    main_photo = models.ImageField(verbose_name="Фото блюда", upload_to='img/dishes')
    text = models.TextField(verbose_name='Описание блюда', blank=True)
    price = models.CharField(default='0', max_length=200, verbose_name='Стоимость( Указываем только цифру)', blank=True)
    weight = models.CharField(default='0', max_length=200, verbose_name='Вес( Указываем только цифру)', blank=True)

    class Meta:
        verbose_name = 'Блюдо страницы (Соус)'
        verbose_name_plural = 'Блюда страницы (Соус)'

    def __str__(self):
        return str(self.title)