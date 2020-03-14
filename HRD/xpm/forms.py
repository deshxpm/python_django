from django import forms
from xpm.models import Employee, Registration




class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Registration
		fields = "__all__"


class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = "__all__"