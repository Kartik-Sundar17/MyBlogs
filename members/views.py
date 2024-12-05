from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, UpdateView
from django.views import generic
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ProfileUpdateForm, ProfilePageForm
from Theblog.models import Profile, Post
import re
import logging
logging.basicConfig(level=logging.DEBUG)


logger = logging.getLogger(__name__)



def login_user(request):
    print("Entering login_user view")
    if request.method == 'POST':
        print("POST request received")
        username = request.POST['username']
        password = request.POST['password']
        print(f"Username: {username}, Password: {password}")
        user = authenticate(username=username, password=password)
        if user is not None:
            print(f"User authenticated: {user.username}")
            login(request, user)
            if user.is_staff:
                print(f"User is staff: {user.username}")
                return redirect('admin:index')  # Redirect to admin
            else:
                print(f"User is not staff: {user.username}")
                return redirect('home')  # Redirect to home
        else:
            print("Authentication failed")
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        print("GET request received")
        return render(request, 'login.html')

# Profile Page
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Profile Page Link
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author=self.object.user)
        context["page_user"] = page_user
        context["user_posts"] = user_posts
        context["post_count"] = user_posts.count()  # Add the post count to the context
        return context

# Profile edit (bio, profile_pic, etc.)
class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('Home')

# Registration
class UserRegisterView(View):
    template_name = 'registration/register.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')

        if not self.is_valid_username(username):
            messages.error(request, 'Invalid username format')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if not self.is_valid_password(password1):
            messages.error(request, 'Password Pattern Invalid')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email exists')
            return redirect('register')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, 'User created successfully! Please login.')
        return redirect('login')

    def is_valid_username(self, username):
        # Regular expression for username validation
        pattern = re.compile(r'^(?=.*[a-zA-Z])(?=.*[0-9_@.+-])[a-zA-Z0-9_@.+-]+$')
        return bool(pattern.match(username))

    def is_valid_password(self, password):
        # Regular expression for password validation
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$')
        return bool(pattern.match(password))


# Settings Update (username, email, etc.)
class UserEditView(generic.UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('Home')

    def get_object(self):
        return self.request.user
    
def delete_selected_posts(request):
    if request.method == 'POST':
        selected_post_ids = request.POST.getlist('selected_posts')
        # Ensure at least one post is selected
        if not selected_post_ids:
            messages.error(request, 'No posts selected.')
            return redirect('user_profile')  # Adjust this redirect URL as per your application

        # Delete selected posts
        try:
            deleted_posts_count = Post.objects.filter(id__in=selected_post_ids).delete()
            messages.success(request, f'{deleted_posts_count} posts deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting posts: {str(e)}')

        return redirect('user_profile')  # Adjust this redirect URL as per your application
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('user_profile')  # Adjust this redirect URL as per your application    






            
# Logout View
def logout_view(request):
    logout(request)
    return redirect('/')

