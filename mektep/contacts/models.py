from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse
# Create your models here.

class CUser(AbstractUser):
    m = "Мужчина"
    w = "Женщина"
    other = "Другой"
    gender_choices = ((m,"Мужчина"),
                      (m,"Женщина"),
                      (other,"Другой"))
    city = models.CharField(max_length=255,verbose_name="Город",blank=True)
    country = models.CharField(max_length=255,verbose_name="Страна",null=True,blank=True)
    birthday = models.DateField(blank=True,null=True,verbose_name="День рождение")
    gender = models.CharField(max_length=15,choices=gender_choices,default="Мужчина",blank=True)
    face = models.ImageField(upload_to="faces/%Y/%m/%d/",verbose_name="Фото",null=True,blank=True)
    interes = models.TextField(verbose_name="Интересы",null=True,blank=True)
    reg_data = models.DateField(auto_now=True,verbose_name="Дата регистрации")
    # images = models.ManyToManyField('Images',verbose_name="Просто картинки" ,blank=True,default="static/img/whoami.png")
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse("profile",kwargs={'pk':self.pk})
class Post(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя поста")
    text = models.TextField(verbose_name="Текст")
    ghost_fio = models.CharField(max_length=70,verbose_name="ФИО")

    public_data = models.DateField(auto_now=True,verbose_name="Дата добавление")
    images = models.ManyToManyField('Images',blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['public_data']
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
    author = models.ForeignKey(CUser, on_delete=models.CASCADE,null=True,blank=True)
    ghost_fio = models.CharField(max_length=70,verbose_name="ФИО",null=True,blank=True)
    content = models.TextField(verbose_name="Комментарий")
    pub_date = models.DateTimeField(auto_now_add=True,verbose_name="Дата")
    def __str__(self):
        return self.content[0:15]
    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"
        ordering = ['pub_date']
class Images(models.Model):
    img = models.ImageField(upload_to="images/",verbose_name="Картинка")
  
    def __name__(self):
        return self.img
    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ['id']
