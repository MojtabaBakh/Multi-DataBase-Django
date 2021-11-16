from django.shortcuts import render
from .models import Book


def Booklist(request):
    # books=Book.objects.all()
    books=Book.objects.using('book_db').all()
    contex={"books" : books}
    return render(request ,"book/list.html" , contex )
