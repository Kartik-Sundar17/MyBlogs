from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from datetime import datetime, date


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    url = models.CharField(max_length=100)
    img = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def img_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%;"/>'.format(self.img_tag))

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=2000)
    title_tag = models.CharField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #content = models.TextField()
    content = models.TextField(max_length=25000)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)  
    img = models.ImageField(null=True, blank=True,upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    snippet=models.CharField(max_length=2550)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} | {self.author.username}"

    def get_absolute_url(self):
        #return reverse('article-detail', args=[str(self.id)])
        return reverse('Home')


class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField()
    profile_pic=models.ImageField(null=True, blank=True,upload_to="posts/profile/")
    website_url = models.CharField(max_length=255, null=True,blank=True)
    facebook_url = models.CharField(max_length=255, null=True,blank=True)
    insta_url = models.CharField(max_length=255, null=True,blank=True)
    twitter_url = models.CharField(max_length=255, null=True,blank=True)
    followers = models.ManyToManyField(User, related_name='following', symmetrical=False, blank=True)

    
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):        
        return reverse('Home')
    def follower_count(self):
        return self.followers.count()

    def following_count(self):
        return self.user.following.count()
    
class Comment(models.Model):
    user = models.ForeignKey(User, null=True, blank=True,related_name="comments", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_comments", blank=True)


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
      
    class Meta:
        ordering = ['-date_added']

        