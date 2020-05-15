from content.models import Category, Content
from home.models import Settings


def category(request):
    return {
        'category': Category.objects.all(),
        'settings': Settings.objects.filter(pk=1),
        'content': Content.objects.all()

    }
