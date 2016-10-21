from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact(request):
    if request.method == 'POST':  # POST METHOD
        form = ContactForm(request.POST, request=request)
        from_email = settings.EMAIL_HOST_USER
        if form.is_valid():
            subject = form.cleaned_data['name'] + " (" + form.cleaned_data['email'] + ") " + form.cleaned_data['subject']
            send_mail(subject,
                      form.cleaned_data['message'],
                      from_email,
                      [from_email],
                      fail_silently=False)
            form.save()
            sform = ContactForm
            messages.success(request, 'Obrigado pelo seu contacto. Iremos responder-lhe em breve.')
            context = {
                "form": sform
            }
            return render(request, "contact.html", context)
        else:
            context = {
                "form": form
            }
            return render(request, "contact.html", context)
    else:  # GET METHOD
        form = ContactForm(request=request)
        context = {
            "form": form
        }
        return render(request, "contact.html", context)

