"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('posts/', views.posts_view),
    path('posts/<int:post_id>/', views.post_detail_view),
    path('posts/create/', views.post_create),
    path('hashtags/', views.hashtags_view),
    path('products/', views.products_view),
    path('categories/', views.categories_view),
    path('products/<int:product_id>/', views.product_detail_view),
    path('products/create/', views.product_create),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
