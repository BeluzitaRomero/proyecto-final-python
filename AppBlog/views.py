from django.shortcuts import render, redirect
from .forms import PostForm, UserForm, CommentForm
from .models import Post, User, Comment
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, UserEditForm

from django.contrib.auth.models import User as UserAuth

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# ---------------------------------------------------------------------------- #
#                            VITAS BASADAS EN CLASES                           #
# ---------------------------------------------------------------------------- #

# class UserList(ListView):
#     model = User
#     template_name = 'AppBlog/users-list-class.html'


# class UserDetail(DetailView):
#     model = User
#     template_name  = 'AppBlog/user-detail.html'

# class UsersCreate(CreateView):
#     model = User
#     template_name = 'AppBlog/new-user.html'
#     success_url = reverse_lazy('class-inicio')
#     fields = ['username', 'name', 'apellido', 'email']

# class UsersUpdate(UpdateView):
#     model = User
#     template_name = 'AppBlog/new-user.html'
#     success_url = reverse_lazy('class-inicio')
#     fields = ['username', 'name', 'apellido', 'email']

# class UserDelete(DeleteView):
#     model = User
#     template_name = 'AppBlog/delete-user.html'
#     success_url = reverse_lazy('class-inicio')

# ---------------------------------------------------------------------------- #
#                          VISTAS BASADAS EN FUNCIONES                         #
# ---------------------------------------------------------------------------- #

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
    print(str(req.user))

    #FORMS incluido en la vista de todos los post
    if req.method == "POST":
        my_form = PostForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data
            new_post = Post(username= req.user,
                            post_description=data['post_description'],
                            post_img=data['post_img'])

            new_post.save()
            return redirect('all-post')
        
    elif req.user.is_authenticated == False:
        return render(req, 'AppBlog/all-post.html', {'all_post': all_post,  })

  
    my_form = PostForm()
    return render(req, 'AppBlog/all-post.html', {'all_post': all_post,'post_form': my_form, 'req': str(req.user)})


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
    # return render(req, "AppBlog/main.html", context)
    return redirect('all-post')


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
        #    post_to_update.username = data['username']

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


###perfil
@login_required
def edit_profile(req):
    user = UserAuth.objects.get(id = req.user.id)

    if req.method == 'POST':
        my_form = UserEditForm(req.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            user.username = data['username']
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            
            user.save()

            return redirect('inicio')

    
    else:
        my_form = UserEditForm(initial = {
                                      'username': user.username,
                                      'email': user.email,
                                      'first_name': user.first_name,
                                      'last_name': user.last_name,
                                       })
    
    return render(req, 'AppBlog/edit-profile.html', {'my_form': my_form, 'user': user})




# ---------------------------------------------------------------------------- #
#                                    UPDATE                                    #
# ---------------------------------------------------------------------------- #
def login_request(req):
    form = AuthenticationForm()

    if req.method == 'POST':
        form = AuthenticationForm(req, data = req.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username = user, password = passw)

            if user is not None:
                login(req, user)
                return render(req, 'AppBlog/main.html', {'message': f'Bienvenido {user}'})

            else:
                return render(req, 'AppBlog/login.html', {'message': f'Error: el usaurio no existe', 'form': form})
        else:
            return render(req, 'AppBlog/login.html', {'message':f'Error, datos incorrectos', 'form':form})
    contexto = {'form': form}
    return render(req, 'AppBlog/login.html', contexto)


def register(req):
    if req.method == 'POST':

        # form = UserCreationForm(req.POST) este es el creado por django con textos
        #por defecto
        form = MyUserCreationForm(req.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(req, 'AppBlog/main.html', {'message': "Usuario creado"})

    else: 
        form = MyUserCreationForm()

    return render(req, 'AppBlog/register.html', {'form': form})





     