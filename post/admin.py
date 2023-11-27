from django.contrib import admin

from post.models import Post, HashTag, Comment, Product, Category, Review


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['hashtags', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'content', 'hashtags__title']

    def has_add_permission(self, request):
        return True


admin.site.register(HashTag)
admin.site.register(Comment)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
