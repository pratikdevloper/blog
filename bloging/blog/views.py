from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .form import Signupform, Loginform,Postform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Post,Contact
# from django.contrib.auth .models import User
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'p': posts})


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        return render(request, 'blog/dashboard.html', {'p': posts})
    else:
        return HttpResponseRedirect('/login')


def about(request):

    return render(request, 'blog/about.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        msg=request.POST.get('message')
        contacts=Contact(name=name,email=email,phone=phone,address=address,message=msg)
        contacts.save()
        messages.success(request,'Thanks for contact Us !!!')


    return render(request, 'blog/contact.html')


def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            messages.success(request, 'Your account is created!!')
            form.save()
    else:
        form = Signupform()
    # form=UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Loginform(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'logged in successfully')
                    return HttpResponseRedirect('/dashboard')
        else:

            form = Loginform()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# add post

def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            post=Postform(request.POST)
            if post.is_valid():
                messages.success(request,'Your Post is Added')
                post.save()
        else:
            post=Postform()
        return render(request, 'blog/addpost.html',{'add':post})
    else:
        return HttpResponseRedirect('/login')

def update_post(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            ip=Post.objects.get(pk=id)
            update=Postform(request.POST,instance=ip)
            if update.is_valid():
                messages.info(request,'Post is updated.....!!!')
                update.save()
        else:
            ip=Post.objects.get(pk=id)
            update=Postform(instance=ip)
        return render(request, 'blog/updatepost.html',{'update':update})
    else:
        return HttpResponseRedirect('/login')



def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            ip=Post.objects.get(pk=id)
            ip.delete()
            return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
