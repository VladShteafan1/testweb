from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    services_list = Service.objects.all()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'services.html', {'services': services_list, 'form': form})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Настройте отправку email
        send_mail(
            f'Сообщение от {name}',
            message,
            email,
            ['your_email@example.com'],  # Замените на ваш email
            fail_silently=False,
        )

        return redirect('contact')
    return render(request, 'contact.html')
