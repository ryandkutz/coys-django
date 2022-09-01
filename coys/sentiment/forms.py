from django import forms


class idForm(forms.Form):
    postID = forms.CharField(label="Enter a post ID", max_length=20)