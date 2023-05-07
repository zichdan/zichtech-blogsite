from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.


class HomePageView(View):
    template_name = "index.html"
    
    def get(self,request):
        posts= Post.objects.all()
        
        context = {
            "posts": posts
        }
        return render(request, self.template_name, context)

class AboutPageView(HomePageView):
    template_name = "about.html"
    
@method_decorator(login_required,"dispatch")
class CreatePostView(View):
    template_name = "createpost.html"
    form_class = PostCreationForm
    initial_values = {"key": "value"}
   
    
    def get(self, request):
        form = self.form_class(initial = self.initial_values)
    
        context = {
        "form": form
    }
        return render (request,"create_post.html", context)


    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
            return redirect('post_home')


def services(request):
    context = {
        "tittle": "About Page"
    }
    return render(request, 'services.html', context)

    
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    context = {"post": post}
    return render(request, "post_detail.html",context)    
    
@login_required
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
    


#  BASIC VIEWS WITHOUT THAT IS NOT CLASS_BASED

# def index(request:HttpRequest):
#     posts = Post.objects.all()
        
#     context = {
#         "posts": posts
#     }
#     return render(request,'index.html', context)



# def about(request):
#     context = {
#         "tittle": "About Page"
#     }
#     return render(request, 'about.html', context)



# @login_required
# def create_post(request):
#     form = PostCreationForm()
    
#     if request.method == "POST":
#         form = PostCreationForm(request.POST, request.FILES)
        
#         if form.is_valid():
#             form.save()
            
#             return redirect('post_home')
#     context={
#         'form': form
#     }
#     return render (request,"create_post.html", context)
    





# tittle = (data['tittle'])
#     content = (data['content'])
#     author = (data['author'])
    
#     new_post = Post(
#         tittle = tittle,
#         content = content,
#         author = author
#     )
#     new_post.save()



