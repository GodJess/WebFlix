from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField("Название", max_length = 30)
    image = models.CharField("Logo", max_length = 200)
    description = models.CharField("описание", max_length = 300)
    release_date = models.CharField("Дата выхода", max_length = 30)
    review = models.CharField("Обзор", max_length = 300)
    countseason = models.CharField("Количество сезонов", max_length=10)
    view = models.CharField("Фильм или Сериал", max_length= 100)
    genre = models.CharField("Жанр", max_length= 100)

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def __str__(self):
        return self.name

class Season1(models.Model):
    serialname = models.CharField("Название сериала", max_length=50)
    linkseries = models.CharField("Ссылка на серию", max_length=300)
    numberseason = models.CharField("Номер сезона", max_length=50)
    prevewimage = models.CharField("Превью серии", max_length=300)
    numberseries = models.CharField("Номер серии", max_length=20)

    def __str__(self):
        return self.serialname
    
    class Meta:
        verbose_name = "Сезон"
        verbose_name_plural = "Сезоны"

class Comment(models.Model):
    loginCom = models.CharField("Логин пользователя", max_length=50)
    serialName = models.CharField("Название сериала", max_length= 50)
    text = models.TextField("Текст комментария", max_length=300)
    like = models.CharField("Лайки", max_length= 10)
    dislike = models.CharField("Дизлайки", max_length= 10)

    def __str__(self):
        return self.serialName
    
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"