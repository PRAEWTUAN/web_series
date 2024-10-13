# series/forms.py
from django import forms
from .models import Series, Comment, Rating

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['title', 'cover_image_url', 'description', 'country', 'average_rating']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
