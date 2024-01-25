from django.contrib import admin
from django.urls import path

from news import views as news


 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news.all_news),
    path('', news.empty),
    path('news/<int:id>/', news.detail),
    path('country/<str:country>/',news.filterCountry),
]