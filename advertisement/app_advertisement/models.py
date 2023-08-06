from django.db import models

# Create your models here.
# Придумате 6 полей к этой сущности
# Заголовки
# описание
# Автор
# Цена
# Дата создания
# Дата обновления
# Торг (уместен или нет)

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    description = models.TextField("Описание")
    author = models.CharField("Автор", max_length=28)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement( id = {self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"
