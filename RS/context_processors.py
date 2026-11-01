from .models import RedesSociales

def redes_sociales(request):
    redes = RedesSociales.objects.all()
    return {'RedesSociales': redes}