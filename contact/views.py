from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

def contacto(request):
    enviado = request.GET.get("enviado") == "1"

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            correo = EmailMessage(
                subject=f"Nuevo mensaje de contacto de {nombre}",
                body=f"De: {nombre} <{email}>\n\n{mensaje}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email],
            )
            correo.send()
            return redirect(f"{reverse('contacto')}?enviado=1")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form, "enviado": enviado})