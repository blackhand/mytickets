# -*- coding: utf-8 -*-
#pylint: disable-msg=E1101

from ticket.models import Event

def image_aref_list(max):
    """
    get a list of image urls from the Event with prominent flag set
    up to max
    """
    image_list = []
    for event in Event.objects.filter(is_prominent=True)[:max]:
        image_list.append(event.image.thumbnail)

    return image_list

        
