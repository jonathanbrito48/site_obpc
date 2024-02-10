from .models import Ministerios

def MinisteriosContext(request):
    return{"ministerios":Ministerios.objects.all()}