from .models import Title, Station


def get_titles(request):
    titles = Title.objects.all()
    return titles

