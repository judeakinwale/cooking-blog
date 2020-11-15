from django import forms


class ContactUsForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label="First Name", max_length=200, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label="Last Name", max_length=200, required=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label="Email Address")
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}), label="Tel. Number", required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
