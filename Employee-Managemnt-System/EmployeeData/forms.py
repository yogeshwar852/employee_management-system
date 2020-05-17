from django.forms import ModelForm
from .models import EmpData


class OrderForm(ModelForm):
	class Meta:
		model = EmpData
		fields = '__all__'