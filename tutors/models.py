from django.db import models

# Create your models here.
class Tutor(models.Model):
    l_name = models.CharField('Фамилия', max_length=100, default='', db_index=True, blank=True)
    f_name = models.CharField('Имя', max_length=100, default='', blank=True)
    fath_name = models.CharField('Отчество', max_length=100, default='', blank=True, null=True)
    img_link = models.URLField('Ссылка на фото', max_length=128, db_index=True, blank=True, null=True)
    anchor = models.CharField('Анкор на сайте', max_length=128, blank=True, null=True)
    city = models.ForeignKey('Cities', verbose_name='Город', null=True, on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subjects', related_name='Предметы')
    school = models.BooleanField('Работает в школе', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['l_name', 'city']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Cities(models.Model):
    name = models.CharField('Город', max_length=100, blank=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class Subjects(models.Model):
    subj_code = models.CharField('Код предмета', max_length=4, blank=True)
    name = models.CharField('Предмет', max_length=100, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name