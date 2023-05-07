from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post


# Create your views here.


def index(request:HttpRequest):
    posts = Post.objects.all()
        
    context = {
        "posts": posts
    }
    return render(request,'index.html', context)

def about(request):
    context = {
        "tittle": "About Page"
    }
    return render(request, 'about.html', context)

def services(request):
    context = {
        "tittle": "About Page"
    }
    return render(request, 'services.html', context)

def create_post(request):
    form = PostCreationForm()
    
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            
            return redirect('post_home')
    context={
        'form': form
    }
    return render (request,"create_post.html", context)
    
    
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    context = {"post": post}
    return render(request, "post_detail.html",context)    
    
    
def update_post(request, post_id):
    post_to_update = Post.objects.get(pk=post_id)
    
    form  = PostCreationForm(instance=post_to_update)
    
    if request.method == 'POST':
        form = PostCreationForm(instance=post_to_update,
            data=request.POST, files=request.FILES
        )
    
    if form.is_valid():
        form.save()
        return redirect("post_home")
    
    context = {
        "form":form
    }
    return render(request, "update.html",context)    
    


# tittle = (data['tittle'])
#     content = (data['content'])
#     author = (data['author'])
    
#     new_post = Post(
#         tittle = tittle,
#         content = content,
#         author = author
#     )
#     new_post.save()



