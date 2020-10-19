from django.forms import ModelForm
from myapp.models import *
from django import forms


class ReporterForm(ModelForm):
    class Meta:
        model = Reporter
        fields = ['name']


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'pub_date': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
        widgets = {
            'products': forms.CheckboxSelectMultiple()
        }


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['name']
        

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'actors': forms.CheckboxSelectMultiple()
        }
                
