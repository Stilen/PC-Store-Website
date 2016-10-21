from django.conf import settings
from django import forms
from contact.models import Contact
from crispy_forms.helper import FormHelper
import urllib.parse as urllib
import urllib.request as urllib2
import json, codecs


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Assunto'}),
            'message': forms.Textarea(attrs={'placeholder': 'Mensagem'}),
        }

    def __init__(self, *args, **kwargs):
        # make the request object available to the form object
        self.request = kwargs.pop('request', None)
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['subject'].label = ''
        self.fields['message'].label = ''

        self.helper = FormHelper()
        self.helper.form_show_labels = False

    def clean(self):
        super(ContactForm, self).clean()

        # test the google recaptcha
        url = "https://www.google.com/recaptcha/api/siteverify"
        values = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': self.request.POST.get(u'g-recaptcha-response', None),
            'remoteip': self.request.META.get("REMOTE_ADDR", None),
        }
        data = urllib.urlencode(values)
        binary_data = data.encode('utf-8')
        req = urllib2.Request(url, binary_data)
        response = urllib2.urlopen(req)
        reader = codecs.getreader('utf-8')
        result = json.load(reader(response))

        # result["success"] will be True on a success
        if not result["success"]:
            raise forms.ValidationError('A validação reCAPTCHA falhou. Por favor tente de novo.')

        return self.cleaned_data
