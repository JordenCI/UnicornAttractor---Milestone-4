from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.core.mail import send_mail
from django.contrib import auth, messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from bugs.models import Bug
from features.models import Feature
from forum.models import ForumPost

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        contact_form = request.POST
        if contact_form.is_valid():
            message = request.POST['message']
            subject = request.POST['subject']
            email_to = request.POST['email']
            send_mail(
                subject,
                message,
                'jordenkv@gmail.com',
                [email_to],
                fail_silently=False,
                )
            messages.success(request, "Your message has been sent! ")
            return render(request, 'contact.html')
        else:
            messages.error(request, "Unable to send message at this time")
    return render(request, 'contact.html')

@login_required    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect (reverse('index'))
    
def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        
@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    bugs = Bug.objects.filter(author=request.user)
    features = Feature.objects.filter(author=request.user)
    posts = ForumPost.objects.filter(author=request.user)
    return render(request, 'profile.html', {'bugs':bugs, 'features':features, 'posts': posts})


