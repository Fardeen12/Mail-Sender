from django import forms

class Sent(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email
