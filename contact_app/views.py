from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_app/success_feedback.html')  # Перенаправление на страницу успеха
    else:
        form = ContactForm()
    return render(request, 'contact_app/contact.html', {'form': form})

def success_feedback(request):
    return render(request, 'contact_app/success_feedback.html')