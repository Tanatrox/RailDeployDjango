from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User

class CambiarPasswordForm(PasswordChangeForm):
	old_password = forms.CharField(label='Contraseña actual: ', required=True, widget=forms.PasswordInput())
	new_password1 = forms.CharField(label='Nueva contraseña: ', required=True, widget=forms.PasswordInput())
	new_password2 = forms.CharField(label='Confirmar contraseña: ', required=True, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ['old_password', 'new_password1', 'new_password2']

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Correo electrónico: ', required=True)

class UserSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label='Nueva contraseña: ', required=True, widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Confirmar contraseña: ', required=True, widget=forms.PasswordInput())

class NewUserForm(UserCreationForm):
	first_name = forms.CharField(label='Nombre(s): ', required=True)
	last_name = forms.CharField(label='Apellido: ', required=True)
	username = forms.CharField(label='Nombre de usuario: ', required=True)
	email = forms.EmailField(label='Correo electrónico: ', required=True)
	password1 = forms.CharField(label='Contraseña: ', required=True, widget=forms.PasswordInput())
	password2 = forms.CharField(label='Confirmar contraseña: ', required=True, widget=forms.PasswordInput())


	class Meta:
		model = User
		fields = ("first_name","last_name", "username", "email", "password1", "password2")
 

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class EditarPerfilForm(UserChangeForm):
	password = None
	first_name = forms.CharField(label='Nombre(s): ')
	last_name = forms.CharField(label='Apellido: ')
	username = forms.CharField(label='Nombre de usuario: ')
	email = forms.EmailField(label='Correo electrónico: ')
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email']

class IniciarSesionForm(AuthenticationForm):
	username = forms.CharField(label='Nombre de usuario: ', required=True)
	password = forms.CharField(label='Contraseña: ', required=True, widget=forms.PasswordInput())
	
	class Meta:
		model=User
		fields = ['username', 'password']



