from django.shortcuts import render, redirect
from myapp.forms import *
from myapp.models import *


def list_reporters(request):
    reporters = Reporter.objects.all()
    return render (request, "list_reporters.html", {'reporters': reporters})


def add_reporter(request):
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_reporters')
    else:
        form = ReporterForm()
        return render(request, "add.html", {'form': form})    
    

def list_articles(request):
    articles = Article.objects.all()
    return render(request, "list_articles.html", {'articles': articles})


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_articles')
    else:
        form = ArticleForm()
        return render(request, "add.html", {'form': form})


def list_clients(request):
    clients = Client.objects.all()
    return render(request, "list_clients.html", {'clients': clients})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_clients')
    else:
        form = ClientForm()
        return render(request, "add.html", {'form': form})


def list_products(request):
    products = Product.objects.all()
    return render(request, "list_products.html", {'products': products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_products')
    else:
        form = ProductForm()
        return render(request, "add.html", {'form': form})
    

def list_purchases(request):
    purchases = Purchase.objects.all()
    return render(request, "list_purchases.html", {'purchases': purchases})


def add_purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_purchases')
    else:
        form = PurchaseForm()
        return render(request, "add.html", {'form': form})


def list_actors(request):
    actors = Actor.objects.all()
    return render(request, "list_actors.html", {'actors': actors})


def add_actor(request):
    if request.method == "POST":
        form = ActorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('list_actors')
    else:
        form = ActorForm()
        return render(request, "add.html", {'form': form})
    

def list_movies(request):
    movies = Movie.objects.all()
    return render(request, "list_movies.html", {'movies': movies})


def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_movies')
    else:
        form = MovieForm()
        return render(request, "add.html", {'form': form})
