from django.shortcuts import render
from django.contrib import messages
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
            messages.success(request, "Message transmitted successfully!")
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
