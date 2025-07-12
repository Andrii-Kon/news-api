# articles/views.py

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer

class ArticleListAPIView(generics.ListAPIView):
    """
    Provides a GET endpoint to list all articles.

    Supports filtering, searching, and ordering through the DjangoFilterBackend,
    SearchFilter, and OrderingFilter respectively.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Define the filter backends to be used for this view.
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Specifies fields that can be used for exact-match filtering.
    filterset_fields = ['title']

    # Specifies fields that will be searched for partial text matches.
    search_fields = ['title', 'summary']

    # Specifies fields that the list can be ordered by.
    ordering_fields = ['title', 'created_at']

class ArticleDetailAPIView(generics.RetrieveAPIView):
    """
    Provides a GET endpoint to retrieve a single article by its primary key (pk).

    The `lookup_field` defaults to 'pk', which is the standard primary key field.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer