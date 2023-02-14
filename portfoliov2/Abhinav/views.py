from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, FormView, TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserContactForm
from .models import (
    HomePageModel, 
    UserAboutPage, 
    PersonalWorkPage,
    ContributionWorkPage,
    PhotographyWorkPage )

class HomePage(ListView):
    model = HomePageModel
    template_name = 'person/home.html'
    context_object_name = 'homes'

class AboutPage(ListView):
    model = UserAboutPage
    template_name = 'person/about.html'
    context_object_name = 'about'

class WorkPage(TemplateView):
    template_name = 'person/work.html'

class PersonalPage(ListView):
    model= PersonalWorkPage
    template_name = 'person/work/personalWork.html'
    context_object_name = 'personal'

class ContributePage(ListView):
    model= ContributionWorkPage
    template_name = 'person/work/contributeWork.html'
    context_object_name = 'contributed'

class PhotographyPage(ListView):
    model= PhotographyWorkPage
    template_name = 'person/work/photographyWork.html'
    context_object_name = 'photography'

class ContactPage(FormView):
    form_class = UserContactForm
    template_name = 'person/contactform.html'
    success_url = '/'

    def form_valid(self, form):
        body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['email'], 
            'message':form.cleaned_data['message'], 
            }
        message = 'Sender Email - {}\n Sender Message - {}'.format(body['email'],body['message'])
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            f'Message from {body["name"]}', 
            message, 
            email_from,
            ['mabhinav534@gmail.com'],
            )  
        messages.success(self.request,'Your message was send successfully',fail_silently=True)
        return super(ContactPage,self).form_valid(form)

