from django import forms

class loginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'p-2 pl-10 w-full rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Nombre de usuario',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'p-2 pl-10 w-full rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': '********',
        })
    )
    tipoUsuario = forms.ChoiceField(
        choices=[('1', 'Estudiante'), ('2', 'Profesor')],
        widget=forms.Select(attrs={
            'class': 'p-2 pl-10 w-full rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
        })
    )
