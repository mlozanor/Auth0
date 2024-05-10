from ..models import Solicitud

def get_solicitudes():
    queryset = Solicitud.objects.all()
    return queryset


def get_solicitud_by_id(id):
    solicitud = Solicitud.objects.raw('SELECT * FROM solicitudes_solicitud WHERE id = %s', [id])
    return solicitud


def create_solicitud(form):
    solicitud = form.save()
    solicitud.save()
    return solicitud