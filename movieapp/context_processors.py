from .models import Category,Movie
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)
