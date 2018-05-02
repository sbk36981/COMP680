from django.forms import ModelForm, ChoiceField
from .models import House

class HouseForm(ModelForm):
    class Meta:
        model = House
        exclude = ['predicted_price']