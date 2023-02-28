from django.urls import path
from AppBlog import views


urlpatterns =[
    path('', views.home, name='inicio'),
    path('users/', views.users, name='users'),
    path('posts/', views.posts, name='posts'),
    path('comments/', views.comments, name='comments'),
#all
    path('all-post/', views.get_all_posts, name='all-post'),
    path('all-users/', views.get_all_users, name='all-users'),
    path('all-comments', views.get_all_comments, name='all-commenst'),

#find 
    path('find-post/', views.find_post, name='find-post'),
    path('find-user/', views.find_user, name='find-user'),
    path('find-comment/', views.find_comment, name='find-comment'),

#forms
    # path('post-form/', views.post_form, name='post-form'),
    path('user-form/', views.user_form, name='user-form'),
    path('comment-form/', views.comment_form, name='comment-form'),

#delete
    path('delete-post/<post_id>', views.delete_post, name='delete-post'),
#update
    path('edit-post/<post_id>', views.update_post,name='edit-post'),


#CLASS
    path('class-inicio/', views.UserList.as_view(), name='class-inicio'),
    path('class-detail/<pk>', views.UserDetail.as_view(), name='class-detail'),
    path('class-new/<pk>', views.UsersCreate.as_view(), name='class-new'),
    path('class-edit/<pk>', views.UsersUpdate.as_view(), name='class-edit'),
    path('class-delete/<pk>', views.UserDelete.as_view(), name='class-delete'),
]
