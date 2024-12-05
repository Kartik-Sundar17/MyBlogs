from django.contrib import admin
from .models import Post,Category,Profile,Comment

#For Config. of CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('img_tag','title','description','url','add_date')
    search_fields = ('title',)

#For Config. of PostAdmin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','title_tag','author','cat')
    search_fields =('title',)
    list_filter =('cat',)
    list_per_page = 50
    
class ProfileAdmin(admin.ModelAdmin):
    list_diplay=('user', ' bio')

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comment)
