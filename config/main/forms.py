from django import forms
from .models import Restaurant


class AddRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        labels = {
            'name': "Название",
            'address': "Адрес",
            'special': "Специализация",
            'phone_number': "Номер"
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'forms-control'}),
            'address': forms.TextInput(attrs={'class': 'forms-control'}),
            'special': forms.TextInput(attrs={'class': 'forms-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'forms-control'})
        }