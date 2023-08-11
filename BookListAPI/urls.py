from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.books),
    path("books", views.BookList.as_view()),
    # path("books/<int:pk>", views.get_Book.as_view()),
    path("books/<int:pk>", views.SingleBookView.as_view()),
]
