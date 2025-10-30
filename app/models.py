from django.db import models
from django.utils import timezone
# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Club(models.Model):
    name = models.CharField(max_length=200, verbose_name="Үйірме атауы")
    description = models.TextField(verbose_name="Сипаттама")
    image = models.ImageField(upload_to='clubs/', verbose_name="Сурет", blank=True, null=True)
    icon = models.CharField(max_length=100, verbose_name="Иконка классы", blank=True, help_text="FontAwesome иконка классы, мысалы: fas fa-code")
    is_active = models.BooleanField(default=True, verbose_name="Белсенді")
    created_at = models.DateTimeField(default=timezone.now)
    order = models.PositiveIntegerField(default=0) 
    class Meta:
        verbose_name = "Үйірме"
        verbose_name_plural = "Үйірмелер"
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    POSITION_CHOICES = [
        ('teacher', 'Мұғалім'),
        ('administrator', 'Әкімшілік'),
        ('director', 'Директор'),
        ('other', 'Басқа'),
    ]
    
    name = models.CharField(max_length=200, verbose_name="Аты-жөні")
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="Лауазымы")
    image = models.ImageField(upload_to='staff/', verbose_name="Сурет")
    description = models.TextField(verbose_name="Сипаттама", blank=True)
    experience = models.IntegerField(verbose_name="Тәжірибесі (жыл)", default=0)
    is_active = models.BooleanField(default=True, verbose_name="Белсенді")
    order = models.IntegerField(default=0, verbose_name="Реттік номер")
    
    class Meta:
        verbose_name = "Қызметкер"
        verbose_name_plural = "Қызметкерлер"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тақырыбы")
    content = models.TextField(verbose_name="Мазмұны")
    image = models.ImageField(upload_to='news/', verbose_name="Сурет", blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Жарияланған күні")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Жаңалық"
        verbose_name_plural = "Жаңалықтар"
        ordering = ['-date']
    
    def __str__(self):
        return self.title

