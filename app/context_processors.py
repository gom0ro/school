from .models import Club

def clubs_processor(request):
    """Барлық үйірмелерді шапкаға шығару үшін"""
    try:
        return {
            'nav_clubs': Club.objects.all().order_by('order', 'name')
        }
    except:
        return {'nav_clubs': []}
