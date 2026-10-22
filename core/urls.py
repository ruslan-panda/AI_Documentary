from django.contrib import admin
from django.urls import path
from . import views  # Импортируем твой файл views.py, который ты только что создал

urlpatterns = [
    path('admin/', admin.site.urls),

    # Пустые кавычки '' означают корень сайта (главную страницу http://127.0.0)
    path('', views.home_page, name='home'),
]
