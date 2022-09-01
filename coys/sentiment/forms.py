from django import forms


class idForm(forms.Form):
    postID = forms.CharField(label="Enter a post ID", max_length=20)
class unameForm(forms.Form):
    uname = forms.CharField(label="Enter a reddit username", max_length=50)