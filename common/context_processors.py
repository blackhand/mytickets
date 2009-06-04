# -*- coding: UTF-8 -*-

from ticket.models import Category

def misc(request):
    """
    Add misc vars
    categories - category list for events
    """
    return {
        'categories': Category.objects.with_ads()
    }

