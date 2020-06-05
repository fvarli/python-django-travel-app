from content.models import Category, Content
from home.models import Settings


def category(request):
    return {
        'category': Category.objects.filter(status='True'),
        'settings': Settings.objects.get(pk=1),
        'content': Content.objects.all()

    }
