from django import forms

class UserForm(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()


class PostForm(forms.Form):
    post_img = forms.CharField()
    post_description = forms.CharField()
    username = forms.CharField()

class CommentForm(forms.Form):
    username = forms.CharField()
    comment = forms.CharField()
