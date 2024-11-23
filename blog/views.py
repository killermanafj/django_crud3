from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Post, NewPost
from django.core.paginator import Paginator
from .forms import NewPostForm
from django.utils import timezone

def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    posts = NewPost.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'posts': posts_list})


def post_detail(request, pk):
    post = get_object_or_404(NewPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def product_detail(request):
    products = [
        {'name': 'Iphone 16 Pro',
         'description': 'Это телефон компании Apple...',
         'price': '150000',
         'created_at': '25.10.2024'},
        {'name': 'Samsung s24 Ultra',
         'description': 'Это телефон компании Samsung...',
         'price': '135000',
         'created_at': '21.10.2024'}
    ]
    paginator = Paginator(products, 1)
    page_number = request.GET.get('test')
    product = paginator.get_page(page_number)

    return render(request, 'blog/product_detail.html', {'product': product})


def about(request):
    return render(request, 'blog/about.html')


def get_contacts(request):
    return render(request, 'blog/contacts.html')


def get_profile(request):
    name = "Денис"
    age = "98"
    location = "СССР"
    return render(request, 'blog/profile.html',
                  {'username': name, 'age': age,
                   'location': location})

def post_new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if NewPost.objects.filter(title=title).exists():
                form.add_error('title', 'Пост с таким заголовком уже существует.')
            else:
                post = form.save(commit=False)
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form = NewPostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request):
    post = get_object_or_404(NewPost, pk=pk)
    if request.method == "POST":
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(cpmmit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = NewPostForm(instance=post)
    return render(request, 'blod/post_edit.html', {'form': form})