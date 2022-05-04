from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Task(models.Model):
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
    )
    pub_date = models.DateTimeField(auto_now=True)
    date_to_complete = models.DateTimeField(blank=True)

    CHOICE_STATUS = [
        ('OP', 'Opening'),
        ('IN', 'In progress'),
        ('DN', 'Done')
    ]
    status = models.CharField('Статус', max_length=2, choices=CHOICE_STATUS, default='OP')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
