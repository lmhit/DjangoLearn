from  django import  forms
from DjangoModel.models import Contact
class ContactForm(forms.Form):
    class META:
        __module__ =  Contact


    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField(required=False)