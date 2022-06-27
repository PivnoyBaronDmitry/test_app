from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=155, verbose_name='Автор', blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    is_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title


class Topping(models.Model):
    FEATURES_CHOICES = [
        ('hot', 'острый'),
        ('vegan', 'вегетерианский'),
    ]
    title = models.CharField(max_length=100, verbose_name='Название')
    features = models.CharField(max_length=100, verbose_name='Свойства', choices=FEATURES_CHOICES, default=None, blank=True)

    class Meta:
        verbose_name = 'Начинка'
        verbose_name_plural = 'Начинки'

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    weight = models.IntegerField(verbose_name='Вес (гр.)')
    toppings = models.ManyToManyField(Topping, blank=True, related_name='pizzas')
    price = models.IntegerField(verbose_name='Цена', blank=True)

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        return self.title
