from django.shortcuts import render, redirect
from django.test import override_settings

from post.forms import PostCreateForm, PostCreateForm2, ProductCreateForm, ProductCreateForm2
from post.models import Post, Product, HashTag, Category


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        # posts = Post.objects.all()  # QuerySet
        posts = Post.objects.prefetch_related('hashtags').all()
        # SELECT * FROM post_post;

        context = {
            "posts": posts,
        }

        return render(request, 'posts/posts.html', context=context)


def post_detail_view(request, post_id):
    if request.method == 'GET':
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {
            "post": post
        }

        return render(request,
                      'posts/post_detail.html',
                      context)


def post_create(request):
    if request.method == 'GET':
        context = {
            "form": PostCreateForm
        }
        return render(request, 'posts/create.html', context)
    if request.method == 'POST':
        form = PostCreateForm2(request.POST, request.FILES)
        if form.is_valid():
            Post.objects.create(**form.cleaned_data)
            return redirect("/posts/")

        context = {
            "form": form
        }

        return render(request, 'posts/create.html', context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()

        context = {
            "hashtags": hashtags,
            "name": "Asyl"
        }

        return render(
            request,
            'posts/hashtags.html',
            context=context
        )


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()  # QuerySet

        context = {
            "products": products,
        }

        return render(request, 'products/products.html', context=context)


@override_settings(DEBUG=True)
def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            "categories": categories,
        }

        return render(
            request,
            'products/categories.html',
            context=context
        )


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {
            "product": product
        }

        return render(request,
                      'products/product_detail.html',
                      context)


def product_create(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm
        }
        return render(request, 'products/create.html', context)
    if request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect("/products/")

        context = {
            "form": form
        }

        return render(request, 'products/create.html', context)
