from django import forms

class AdventureForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)
    mode = forms.CharField(max_length=100, required=True)


class PuzzleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)
    mode = forms.CharField(max_length=100, required=True)


class RetroForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)
    mode = forms.CharField(max_length=100, required=True)


class RpgForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)


class StealthForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)
    mode = forms.CharField(max_length=100, required=True)


class SurvivalForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    developer = forms.CharField(max_length=100, required=True)
    platform = forms.CharField(max_length=100, required=True)
    mode = forms.CharField(max_length=100, required=True)


class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    surname = forms.CharField(max_length=100, required=True)
    user_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

# class LoginForm(forms.Form):
#     user_name = forms.CharField(max_length=65)
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)



