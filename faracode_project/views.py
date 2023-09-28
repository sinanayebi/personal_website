from django.shortcuts import render
from resumes_app.models import Project
from contactus_app.models import Footer, SendMessage


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        SendMessage.objects.create(name=name, email=email, subject=subject, message=message)

    projects = Project.objects.all()
    footer = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects': projects, 'footer': footer})

