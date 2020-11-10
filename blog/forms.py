from django import forms


class ContactUsForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=200)
    last_name = forms.CharField(label="Last Name", max_length=200)
    email = forms.EmailField(label="Email Address", required=False)
    phone = forms.IntegerField(label="Tel. Number", required=False)
    message = forms.Textarea()
