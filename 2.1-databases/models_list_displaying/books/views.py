from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    
        
    var_book = Book.objects.all().order_by('pub_date') 
    books = []
    for var in var_book:
      books.append({'name':var.name, 'author':var.author, 'pub_date':var.pub_date})
    #   print (books) 
    
    var1 = request.GET.get("books", var.pub_date)
    
      
    paginator = Paginator (books,5)
    page = paginator.get_page(var1)
    context = {
              'page': page,
              }
    
    # context = {'books' : books}
    return render(request, template, context)


def books_cat(request):
    template = 'books/books_catalog.html'
    
        
    var_book = Book.objects.all().order_by('pub_date') 
    books = []
    for var in var_book:
      books.append({'name':var.name, 'author':var.author, 'pub_date':var.pub_date})
    #   print (books) 
    
    var1 = request.GET.get("books", var.pub_date)
    
      
    paginator = Paginator (books)
    page = paginator.get_page(var1)
    context = {
              'page': page,
              }
    
    # context = {'books' : books}
    return render(request, template, context)
