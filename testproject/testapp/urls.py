from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('news/all', NewsAPIGenericView.as_view()),
    path('news/<int:pk>', NewsAPIUpdateView.as_view()),

    # path('news/all/', NewsAPIView.as_view({'get': 'list'})),
    # path('test/', ListNews.as_view()),

    # path('pizza/all', PizzaAPIView.as_view()),


]