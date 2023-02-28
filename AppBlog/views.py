from django.shortcuts import render, redirect
from .forms import PostForm, UserForm, CommentForm
from .models import Post, User, Comment
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# ---------------------------------------------------------------------------- #
#                            VITAS BASADAS EN CLASES                           #
# ---------------------------------------------------------------------------- #

class UserList(ListView):
    model = User
    template = 'AppBlog/users-list.html'


class UserDetail(DetailView):
    model = User
    template  = 'AppBlog/user-detail.html'

class UsersCreate(CreateView):
    model = User
    template = 'AppBlog/new-user.html'
    success = reverse_lazy('class-inicio')
    fields = ['username', 'name', 'apellido', 'email']

class UsersUpdate(UpdateView):
    model = User
    template = 'AppBlog/new-user.html'
    success = reverse_lazy('class-inicio')
    fields = ['username', 'name', 'apellido', 'email']

class UserDelete(DeleteView):
    model = User
    success_url = 'AppBlog/'


def home(req):
    return render(req, 'AppBlog/main.html')


def users(req):
    return render(req, 'AppBlog/users.html')


def posts(req):
    return render(req, 'AppBlog/posts.html')


def comments(req):
    return render(req, 'AppBlog/comments.html')

# ---------------------------------------------------------------------------- #
#                                    GET ALL                                   #
# ---------------------------------------------------------------------------- #


def get_all_posts(req):
    all_post = Post.objects.all()

    #FORMS incluido en la vista de todos los post
    if req.method == "POST":
        my_form = PostForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_post = Post(username=data['username'],
                            post_description=data['post_description'],
                            post_img=data['post_img'])

            new_post.save()
            return redirect('all-post')

    my_form = PostForm()
    return render(req, 'AppBlog/all-post.html', {'all_post': all_post, 'post_form': my_form})


def get_all_users(req):
    all_user = User.objects.all()

    return render(req, 'AppBlog/all-users.html', {'all_users': all_user})


def get_all_comments(req):
    get_all_comments = Comment.objects.all()

    return render(req, 'AppBlog/all-comments.html', {'all_comments': get_all_comments})


# ---------------------------------------------------------------------------- #
#                                     FIND                                     #
# ---------------------------------------------------------------------------- #
def find_post(req):
    if req.GET['username']:
        post_to_find = req.GET['username']
        post = Post.objects.filter(username__icontains=post_to_find)

        return render(req, 'AppBlog/post-results.html', {'post': post, 'username': post_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)


def find_user(req):
    if req.GET['username']:
        user_to_find = req.GET['username']
        user = User.objects.filter(username__icontains=user_to_find)

        return render(req, 'AppBlog/user-results.html', {'users': user, 'username': user_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)


def find_comment(req):
    if req.GET['username']:
        comment_to_find = req.GET['username']
        comment = Comment.objects.filter(username__icontains=comment_to_find)

        return render(req, 'AppBlog/comment-results.html', {'comments': comment, 'username': comment_to_find})

    else:
        respuesta = "No se encontro informacion"

    return HttpResponse(respuesta)

# ---------------------------------------------------------------------------- #
#                                     FORMS                                    #
# ---------------------------------------------------------------------------- #


# def post_form(request):
#     if request.method == "POST":
#         my_form = PostForm(request.POST)

#         if my_form.is_valid():
#             data = my_form.cleaned_data
#             new_post = Post(username=data['username'],
#                             post_description=data['post_description'],
#                             post_img=data['post_img'])

#             new_post.save()
#             return redirect('inicio')

#     my_form = PostForm()
#     return render(request, 'AppBlog/post-form.html', {'post_form': my_form})


def user_form(request):
    if request.method == "POST":
        my_form = UserForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_user = User(username=data['username'],
                            name=data['name'],
                            apellido=data['apellido'],
                            email=data['email'])

            new_user.save()
            return redirect('inicio')

    my_form = UserForm()
    return render(request, 'AppBlog/user-form.html', {'user_form': my_form})


def comment_form(request):
    if request.method == "POST":
        my_form = CommentForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_comment = Comment(username=data['username'],
                                  comment=data['comment'])

            new_comment.save()
            return redirect('inicio')

    my_form = CommentForm()
    return render(request, 'AppBlog/comment-form.html', {'comment_form': my_form})


# ---------------------------------------------------------------------------- #
#                                    DELETE                                    #
# ---------------------------------------------------------------------------- #
def delete_post(req, post_id):
    post_to_delete = Post.objects.get(id = post_id)
    post_to_delete.delete()

    #vuelvo al listado de posts
    all_posts = Post.objects.all()

    context = {'all_post': all_posts}
    return render(req, "AppBlog/all-post.html", context)


# ---------------------------------------------------------------------------- #
#                                    UPDATE                                    #
# ---------------------------------------------------------------------------- #
def update_post(req, post_id):
    #post que vamos a modificar
    post_to_update = Post.objects.get(id = post_id)

    if req.method == 'POST':
       my_form = PostForm(req.POST) #Toda la info cargada de ese post

       if my_form.is_valid():
           data = my_form.cleaned_data

           post_to_update.post_img=data['post_img']
           post_to_update.post_description=data['post_description']
           post_to_update.username = data['username']

           post_to_update.save()

           all_posts = Post.objects.all() 

           #!
           #!LA CLAVE ES all_post EN SINGULAAAAAR
           #! tanto tiempo perdido por no ver que tenia una S de maaas!
           #!
           context = {'all_post': all_posts}

           return render(req, 'AppBlog/all-post.html', context)
       
    #en caso de que el metodo no sea post
    else:
        my_form = PostForm(initial={'post_img': post_to_update.post_img,
                                     'post_description': post_to_update.post_description,
                                     'username':post_to_update.username})
        all_posts = Post.objects.all() 
        context = {'my_form':my_form, 'post_id': post_id, 'all_post': all_posts}
        print("MIRAR ACA ALL POST", all_posts)
        
        #voy al html que me permite editar
        return render(req, 'AppBlog/edit-post.html', context)





     