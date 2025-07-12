# articles/urls.py

from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView

app_name = 'articles' # Namespace for the URLs

urlpatterns = [
    # Endpoint for the list of all articles.
    path('', ArticleListAPIView.as_view(), name='article-list'),

    # Endpoint for a single article, identified by its integer primary key.
    path('<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),
]