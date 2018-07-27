from django import forms
from dataStorage.models import EmployeeInfo

#Create Model form
class EmployeeInfoForm(forms.ModelForm):
	firstname = forms.CharField(max_length=128, required=True,  help_text="Please enter First name", widget=forms.TextInput(attrs={"class":"form-control", "style":"width:30%"}))
	lastname = forms.CharField(max_length=128, required=True,  help_text="Please enter Last name", widget=forms.TextInput(attrs={"class":"form-control", "style":"width:30%"}))
	email = forms.EmailField(max_length=128, required=True,  help_text="Please enter Email Address", widget=forms.TextInput(attrs={"class":"form-control", "style":"width:30%"}))

	class Meta:
		model = EmployeeInfo
		fields = ('firstname', 'lastname', 'email',)

	def clean_email(self):
		#Get the email
		email= self.cleaned_data.get('email')

		#Check to see if any users already exist with this email
		#Firstname and Lastname wasn't validated since two people can have the same name
		try:
			match = EmployeeInfo.objects.get(email=email)
		except:
			#Unable to find a user, this is fine
			return email

		#A user was found with this email
		raise forms.ValidationError('This email address is already in use.')