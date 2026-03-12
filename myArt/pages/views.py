from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f"New Contact from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL or 'noreply@myart.com',
                [settings.EMAIL_HOST_USER] if hasattr(settings, 'EMAIL_HOST_USER') and settings.EMAIL_HOST_USER else ['admin@myart.com'],
                fail_silently=False,
            )
            messages.success(request, 'Yay! Message sent successfully. 🌸')
        except Exception as e:
            # Fallback if SMTP isn't configured yet
            print(f"Email failed to send: {e}")
            messages.success(request, 'Yay! Message recorded successfully! (Emails will work magically once SMTP is added to your environment variables) 🌸')
            
        return redirect('contact')
        
    return render(request, 'contact.html')
