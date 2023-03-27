from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView
from .models import *
from .forms import *

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

import random



class Index(ListView):

    paginate_by = 5
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self, *args, **kwargs):
        qs = super(Index, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        
        try:
            if self.request.GET["lang"]=="kz":
                data['lang'] = True
            else:
                data['lang'] = False
        except:
            data['lang'] = False

        return data


# class ProfileEdit(UpdateView):
#     model = CUser
#     template_name = "profileedit.html"
#     form_class = ProfileChange

#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user != self.get_object():
#             return redirect('index')
#         return super().dispatch(request, *args, **kwargs)

def logoutview(request):
    logout(request)
    return render(request,"logout.html")




def about(request):

    try:
        if request.GET["lang"]=="kz":
            lang = True
        else:
            lang = False
    except:
        lang = False
    return render(request,"about.html",context={"lang":lang})


def postadd(request):
    if request.method == "POST":
        print(request.POST["name"])
        post = Post(name=request.POST["name"],text=request.POST["text"],ghost_fio=request.POST["ghost_fio"])
        post.save() # save the post instance
        # loop over the list of images and save each one to the database
        for img in request.FILES.getlist('images'):
            imgs = Images(img=img)
            imgs.save()
            post.images.add(imgs)
        post.save() # save the post instance again after adding the images
        return redirect("/post/"+str(post.pk))



def parent_comment(request,id):
    if request.method=="POST":
        if request.user.pk:
            comment_parent = Comment(author=request.user,post=Comment.objects.get(pk=int(id)).post,content=request.POST["content"],parent_comment=Comment.objects.get(pk=int(id)))
            comment_parent.save()
        else:
            comment_parent = Comment(ghost_fio=request.POST["ghost_fio"],post=Comment.objects.get(pk=int(id)).post,content=request.POST["content"],parent_comment=Comment.objects.get(pk=int(id)))
            comment_parent.save()
    return redirect("/post/"+str(comment_parent.post.pk))

def commentadd(request,id):

    if request.method == "POST":
        if request.user.pk:
            comment = Comment(post=Post.objects.filter(pk=int(id))[0],author=request.user,content=request.POST['content'])
            comment.save()
        else:
            comment = Comment(post=Post.objects.filter(pk=int(id))[0],ghost_fio=request.POST["ghost_fio"],content=request.POST['content'])
            comment.save()
    return redirect("/post/"+str(id))


class PostView( DetailView):
    template_name="post.html"
    model=Post
    context_object_name="post"

