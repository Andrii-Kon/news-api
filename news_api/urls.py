# news_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include all URLs from the 'articles' app under the 'api/articles/' prefix.
    # This creates a modular and organized URL structure.
    path('api/articles/', include('articles.urls', namespace='articles-api')),
]