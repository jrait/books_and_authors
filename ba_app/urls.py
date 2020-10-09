from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('process',views.process),
    path('authors',views.authors),
    path('books/<int:book_id>',views.book_info),
    path('add_info',views.add_info),
    path('authors/<int:author_id>',views.author_info)
]