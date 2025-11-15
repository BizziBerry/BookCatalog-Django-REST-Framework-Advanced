from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import RetrieveAPIView
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer, CategoryDetailSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view  # Раскомментировано

# Представления для книг
@extend_schema(  # Раскомментировано
    summary="Получение списка книг",
    description="Этот эндпоинт позволяет получить список всех книг в базе данных. "
                "Вы также можете добавить новую книгу с помощью POST-запроса.",
    responses={200: BookSerializer(many=True)}
)
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema(  # Раскомментировано
    summary="Работа с конкретной книгой",
    description="Позволяет получить информацию о книге, обновить её данные или удалить.",
    responses={
        200: BookSerializer,
        204: None
    }
)
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной книгой: просмотр, обновление и удаление.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Представления для категорий
@extend_schema(  # Раскомментировано
    summary="Получение списка категорий",
    description="Этот эндпоинт позволяет получить список всех категорий в базе данных. "
                "Вы также можете добавить новую категорию с помощью POST-запроса.",
    responses={200: CategorySerializer(many=True)}
)
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(  # Раскомментировано
    summary="Работа с конкретной категорией",
    description="Позволяет получить информацию о категории, обновить её данные или удалить.",
    responses={
        200: CategorySerializer,
        204: None
    }
)
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной категорией: просмотр, обновление и удаление.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Новое представление для детального просмотра категории с книгами
@extend_schema_view(  # Раскомментировано
    get=extend_schema(
        description="Получение категории с вложенными данными (книги в категории).",
        summary="Детальная категория с книгами"
    )
)
class CategoryDetailView(RetrieveAPIView):
    """
    Представление для получения категории со списком всех книг в этой категории.
    """
    queryset = Category.objects.prefetch_related('books')
    serializer_class = CategoryDetailSerializer