from myapp.views import articles, articles_archives, article_main, article_archive_main, articles_name

from django.urls import path

urlpatterns = [
    path('', article_main),
    path('archive/', article_archive_main),
    path('<int:article_id>/', articles),
    path('<int:articles_archives_id>/archive/', articles_archives),
    path('<int:article_id>/<slug:name>/', articles_name),
]