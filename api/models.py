from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    published_date = models.DateField(verbose_name="Дата публикации")
    # УБЕДИТЕСЬ ЧТО ЭТА СТРОКА ЕСТЬ:
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books", verbose_name="Категория")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    page_count = models.IntegerField(blank=True, null=True, verbose_name="Количество страниц")
    cover = models.URLField(blank=True, verbose_name="Обложка")
    
    def __str__(self):
        return self.title