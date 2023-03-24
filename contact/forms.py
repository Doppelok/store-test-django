from django import forms
from .models import ContactFeedBack
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFeedBack
        fields = ['name', 'email', 'subject', 'message']

    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "data-validation-required-message": "Please enter your name",
        "placeholder": "Your Name"
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control", "data-validation-required-message": "Please enter your email",
        "placeholder": "Your Email"
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control", "data-validation-required-message": "Please enter a subject",
        "placeholder": "Subject"
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control", "rows": 8, "data-validation-required-message": "Please enter your message",
        "placeholder": "Message"
    }))

    def send_email(self):
        theme = self.cleaned_data.get("subject")
        text = f"Hi, {self.cleaned_data.get('name')}! We receive your feedback and contact you soon!"
        send_mail(
            subject=theme,
            message=text,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.cleaned_data.get("email")],
            fail_silently=False,
        )

        ContactFeedBack.objects.create(name=self.cleaned_data.get('name'),
                                       email=self.cleaned_data.get("email"),
                                       subject=self.cleaned_data.get("subject"),
                                       message=self.cleaned_data.get("message"))
