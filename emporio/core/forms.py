from django import forms
from .models import Producto
from django.core import validators

class FormularioIngresoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'




# class FormularioProducto(forms.Form):
#     codigo = forms.IntegerField(validators=[validators.integer_validator])
#     nombre = forms.CharField()
#     #categoria = forms.ChoiceField()
#     contenido = forms.CharField()
#     #presentacion = forms.ChoiceField()
#     precioVenta = forms.IntegerField(validators=[validators.integer_validator])
#     #foto = forms.ImageField()
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MinLengthValidator(0)])
