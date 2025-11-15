from rest_framework import serializers
from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'category', 'isbn', 'page_count', 'cover']
       # extra_kwargs = {
         #   'title': {'help_text': 'Название книги'},
         #   'author': {'help_text': 'Автор книги'},
         #   'published_date': {'help_text': 'Дата публикации (формат YYYY-MM-DD)'},
          #  'category': {'help_text': 'Категория книги'},
          #  'isbn': {'help_text': 'Уникальный ISBN номер книги'},
          #  'page_count': {'help_text': 'Количество страниц'},
         #   'cover': {'help_text': 'Ссылка на изображение обложки'},
       # }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        #extra_kwargs = {
           # 'name': {'help_text': 'Название категории'},
            #'description': {'help_text': 'Описание категории'},
       # }

class CategoryDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'books']
       # extra_kwargs = {
         #   'name': {'help_text': 'Название категории'},
         #   'description': {'help_text': 'Описание категории'},
         #  'books': {'help_text': 'Список книг в этой категории'},
       # }