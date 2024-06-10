from django.db import models

# Create your models here.
class UserData(models.Model):
    login = models.CharField("Логин", max_length= 100)
    name = models.CharField("Имя", max_length= 100)
    surname = models.CharField("Фамилия", max_length= 100)
    mail = models.CharField("Почта", max_length= 100)
    password = models.CharField("Пароль", max_length= 100)
    image = models.CharField("Шапка прфиля", max_length= 100)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.login
    
class UserStat(models.Model):
    login = models.CharField("Логин", max_length = 100)
    science = models.CharField("Наука", max_length= 100)
    kriminal = models.CharField("Криминал", max_length= 100)
    comedy = models.CharField("Комедии", max_length= 100)
    horror = models.CharField("Ужасы", max_length= 100)
    multfilm = models.CharField("Мультфильмы", max_length= 100)
    dram = models.CharField("Фантастика", max_length= 100)
    fantazy = models.CharField("Драммы", max_length= 100)
    serial = models.CharField("Сериалы", max_length= 100)
    film = models.CharField("Фильмы", max_length= 100)

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"

    def __str__(self):
        return self.login