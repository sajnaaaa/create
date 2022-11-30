from . import views
from django.urls import path

app_name = 'createapp'
urlpatterns = [

    path('', views.create, name='create'),
    path('books/<int:books_id>/', views.detail, name='detail'),
    path('add/', views.add_books, name='add_books'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]
