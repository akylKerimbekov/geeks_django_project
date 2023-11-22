from django.shortcuts import render

from post.models import Post, Product


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()  # QuerySet

        context = {
            "posts": posts,
        }

        return render(request, 'posts/posts.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()  # QuerySet

        context = {
            "products": products,
        }

        return render(request, 'products/products.html', context=context)
