from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contacto(request):
    enviado = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            asunto = f'Nuevo mensaje de contacto: {nombre}'

            contenido = (
                f'Nombre: {nombre}\n'
                f'Correo: {email}\n\n'
                f'Mensaje:\n{mensaje}'
            )

            send_mail(
                asunto,
                contenido,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            enviado = True
            form = ContactForm()

    else:
        form = ContactForm()

    return render(
        request,
        'contact/contact.html',
        {'form': form, 'enviado': enviado}
    )


