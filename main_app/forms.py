from django.forms import ModelForm
from .models import Shows

class ShowsForm(ModelForm):
    class Meta:
        model = Shows
        fields = '__all__'