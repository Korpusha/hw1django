from django.urls import path, include
from myapp.views import main, users, users_main, main_regex, num_tel, index, test
from django_proj.article_urls import urlpatterns as article_patterns


urlpatterns = [
    path('', main),
    path('index/', index),
    path('test/', test, name='test'),
    path('article/', include(article_patterns)),

    path('users/', users_main),
    path('users/<int:user>/', users),

    path('phone/<slug:num>/', num_tel),
    path('symbols/<slug:num>/', main_regex),
]
