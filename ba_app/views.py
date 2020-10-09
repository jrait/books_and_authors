from django.shortcuts import render,redirect
from ba_app.models import *

# Create your views here.
def index(request):
    context = {
        'all_books':Books.objects.all(),
    }
    return render(request,'index.html',context)

def process(request):
    if request.POST['form_for'] == 'authors':
        Authors.objects.create(first_name =request.POST['first_name'],last_name =request.POST['last_name'],notes = request.POST['notes'])
        return redirect('/authors')
    else:
        Books.objects.create(title = request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def authors(request):
    context = {
        'all_authors':Authors.objects.all(),
    }
    return render(request,'authors.html',context)

def book_info(request,book_id): 
    context = {
        'book':Books.objects.get(id=book_id),
        'all_authors':Authors.objects.all()
    }
    return render(request,'book_info.html',context)

def author_info(request,author_id):
    context = {
        'author':Authors.objects.get(id=author_id),
        'all_books':Books.objects.all()
    }
    return render(request,'author_info.html',context)

def add_info(request):
    book_to_update = Books.objects.get(id=int(request.POST['book_id']))
    author_to_update = Authors.objects.get(id = request.POST['author_id'])
    book_to_update.authors.add(author_to_update)
    if request.POST['which_page'] == 'author':
        return redirect(f'/authors/{author_to_update.id}')
    else:
        return redirect(f'/books/{book_to_update.id}')