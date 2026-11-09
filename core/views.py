from django.shortcuts import render, get_object_or_404
from Servicios.models import Services
from blog.models import Post, Category
from .models import Politicas

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/../contact/templates/contact/contact.html')

def blog(request):
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    return render(request, 'blog/blog.html', {
        'Posts': posts,
        'Category': categories,
    })

def category_posts(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(
        categories=category,
        published=True
    )
    return render(request, 'blog/category_posts.html', {
        'Posts': posts,
        'category': category,
    })

def services(request):
    return render(request, 'servicios/services.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'servicios/services.html', {
        'services': services
    })

def store(request):
    return render(request, 'core/store.html')

def politicas(request):
    return render(request, 'core/politicas.html')

def privacidad(request):
    politica = get_object_or_404(Politicas, tipo='privacidad')
    return render(request, 'core/politicas.html', {'politica': politica})

def cookies(request):
    politica = get_object_or_404(Politicas, tipo='cookies')
    return render(request, 'core/politicas.html', {'politica': politica})

def aviso_legal(request):
    politica = get_object_or_404(Politicas, tipo='legal')
    return render(request, 'core/politicas.html', {'politica': politica})
