from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    if request.method == "GET":
        context ={
            'books':Book.objects.all()
        }
        return render(request, 'books_app/index.html',context)
    if request.method == 'POST':
        title_name = request.POST['title']
        description = request.POST['desc']
        Book.objects.create(title = title_name, desc = description)
        return redirect('/')
def view(request, books_id):
    if request.method == "GET":
        books_desc = {
            'book': Book.objects.get(id = books_id),
             'authors': Author.objects.all()
        }
        return render(request, 'books_app/desc.html', books_desc)
    if request.method == 'POST':
        book = Book.objects.get(id = books_id)
        author = Author.objects.get(id = request.POST['author_id'])
        book.authors.add(author)
        return redirect('/books/'+books_id)

def authors(request):
    if request.method == 'GET':
        context = {
            'authors': Author.objects.all()
        }
        return render(request, 'books_app/authors.html', context)
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        note = request.POST['notes']
        Author.objects.create(first_name =fname, last_name= lname, notes = note)
        return redirect('/authors')
def notes(request, authors_id):
    if request.method == "GET":
        authors ={
            'author': Author.objects.get(id = authors_id),
            'books': Book.objects.all()
        } 
        return render(request, 'books_app/notes.html', authors)
    # if request.method == 'POST':
    #     author = Author.objects.get(id = authors_id)
    #     book = Book.objects.get(id = request.POST['book_id'])
    #     author.books.add(book)
    #     return redirect('/authors/'+authors_id)
