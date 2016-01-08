from django.views.generic import CreateView
from .models import Publicacion

class RegistrarPublicacion(CreateView):
		template_name = 'pantillas/RegistrarPublicacion.html'
		model = Publicacion

class ReportarPublicacion(ListView):
	template_name= 'principal/ReportarPublicacion.html'
	model = Publicacion