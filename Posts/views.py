from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .forms import PostCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator



# Create your views here.


class HomePageView(View):
    template_name = "index.html"
    
    def get(self,request):
        posts= Post.objects.all()
        
        paginator = Paginator(posts,3)
        
        page_number = request.GET.get("page")
        
        page_obj = paginator.get_page(page_number)
                
        context = {
            "posts": page_obj
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

# def delete_post(request, post_id):
#     post_to_delete = get_object_or_404(Post, pk=post_id)
#     post_to_delete.delete()
#     return redirect(reverse('post_home'))


def delete_post(request, post_id):
    post_to_delete = Post.objects.get(pk=post_id)
    
    if post_to_delete:
        try:
            post_to_delete.delete()
            return redirect(reverse('post_home'))       
            
        except:
            return ("An Error occurred while trying to delete the")
    return ("Post ID Not Found")       


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



