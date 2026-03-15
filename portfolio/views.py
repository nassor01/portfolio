from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, Project, Skill
from .forms import ContactForm

def home(request):
    try:
        profile = Profile.objects.first()
        projects = Project.objects.all()
        skills = Skill.objects.all()
        
        skills_dict = {
            'Design': skills.filter(category='Design'),
            'Development': skills.filter(category='Development'),
        }
    except Exception as e:
        profile = None
        projects = []
        skills_dict = {'Design': [], 'Development': []}
        print(f"Database error: {e}")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            
            subject = f"Portfolio Contact Form: {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    ['mohammadnassor1@gmail.com'],
                    fail_silently=False,
                )
                messages.success(request, "Message transmitted successfully!")
            except Exception as e:
                print(f"Email error: {e}")
                messages.error(request, "Error transmitting message. Please try again later.")
        else:
            messages.error(request, "Error transmitting message. Please check the details.")
    else:
        form = ContactForm()
    
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills_dict,
        'form': form,
    }
    return render(request, 'index.html', context)
