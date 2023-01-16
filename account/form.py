from django.core.exceptions import ValidationError
from django.core import validators
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Your Nmber or Your Email'}) , required=True , validators=[validators.MaxLengthValidator(40)])
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':'Password'}) , required=True)

class SignupForms(forms.Form):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Your Nmber'}) , required=True , validators=[validators.MaxLengthValidator(40)])
    # password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':'Password'}) , required=True)
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) < 11:
            raise ValidationError("you should send the invalid  %(value)s phone number",
            code="invalid_phone_number",
            params={'value': f'{phone}'}
            )
        if phone[0] != '0' :
            raise ValidationError("you should send the invalid  %(value)s phone numbers",
            code="invalid_phone_number",
            params={'value': f'{phone}'})
        return phone

        return phone
class CheckOtpCodes(forms.Form):
    code = forms.CharField(widget = forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Your Code'}) , required=True , validators=[validators.MaxLengthValidator(4)])
    # password = forms.CharField(widget = forms.PasswordInput(attrs={'class': 'form-control' , 'placeholder':'Password'}) , required=True)
