from django import forms
from django.contrib.auth.models import User
from .models import Producto
from django.core import validators


class FormularioIngresoProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
#    rep_password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


    # def clean(self):
    #     all_clean_data = super().clean()
    #     password = all_clean_data['password']
    #     rep_password = all_clean_data['repeat_password']
    #
    #     if password != rep_password:
    #         raise forms.ValidationError("¡¡¡Contraseñas no coinciden!!!")

