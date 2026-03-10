from django.shortcuts import render
from portfolio.models import Profile, Project, Skill

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'profile': profile,
        'projects': projects,
        'skills': {
            'Design': skills.filter(category='Design'),
            'Development': skills.filter(category='Development'),
        }
    }
    return render(request, 'index.html', context)
