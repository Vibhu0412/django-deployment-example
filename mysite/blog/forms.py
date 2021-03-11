from django import forms
from blog.models import Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author' : forms.TextInput(attrs={'class': 'textinputclass'}),
            'text' : forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }


###REGISTER FORM####
class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email","password1","password2")

    def save(self,commit=True):
        user = super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
