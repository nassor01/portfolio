import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from portfolio.models import Profile, Project, Skill
from django.core.files import File

# Create Profile (Masculine adaptation of Kimberly's profile)
profile, created = Profile.objects.get_or_create(
    name="Nassoro Mohammad",
    defaults={
        "role": "Full Stack Architect | UI/UX Designer | Tech Strategist",
        "bio": "Building high-performance digital solutions with technical precision and architectural excellence. Focused on creating scalable, user-centric experiences that redefine modern standards.",
        "email": "mohammadnassor1@gmail.com",
        "location": "Global / Remote",
        "instagram_url": "https://www.instagram.com/nxssorr",
        "github_url": "https://github.com/",
        "linkedin_url": "https://linkedin.com/",
        "twitter_url": "https://twitter.com/",
        "phone": "0792404979",
    }
)

# Update existing profile if fields are different
profile.role = "Full Stack Architect | UI/UX Designer | Tech Strategist"
profile.bio = "Building high-performance digital solutions with technical precision and architectural excellence. Focused on creating scalable, user-centric experiences that redefine modern standards."
profile.instagram_url = "https://www.instagram.com/nxssorr"
profile.phone = "0792404979"
profile.save()

# Set Avatar if it exists
avatar_path = r'C:\Users\moham\.gemini\antigravity\brain\16408c44-c7f7-45c1-9cde-6314cf39aac6\nassoro_avatar_1773174008276.png'
if os.path.exists(avatar_path) and not profile.avatar:
    with open(avatar_path, 'rb') as f:
        profile.avatar.save('nassoro_avatar.png', File(f), save=True)

# Create Skills
print("Cleaning up old Skills and Projects...")
Skill.objects.all().delete()
Project.objects.all().delete()

skills_data = [
    ('Web Design', 'Design'),
    ('UI Design', 'Design'),
    ('HTML', 'Development'),
    ('React', 'Development'),
    ('JavaScript', 'Development'),
    ('CSS', 'Development'),
    ('Django', 'Development'),
]

for name, category in skills_data:
    Skill.objects.get_or_create(name=name, category=category)

# Create initial Projects
projects_data = [
    {
        "title": "Booking System",
        "description": "A comprehensive booking management system developed with modern web technologies for seamless scheduling.",
        "tags": "React, JavaScript, CSS, HTML",
        "order": 1
    }
]

for p_data in projects_data:
    Project.objects.get_or_create(title=p_data['title'], defaults=p_data)

print("Masculine portfolio database populated successfully!")
