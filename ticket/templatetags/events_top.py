# -*- coding: UTF-8 -*-
#pylint: disable-msg=E1101

"""
this template tag get the prominent events for:
    image_cycle_show
"""

from django.template import Library
from ticket.constants import MAX_CYCLE_IMAGES
from ticket.utils import image_aref_list

register = Library()

@register.inclusion_tag('ticket/_image_cycle_show.html')
def image_cycle_show(max_cycle_images=MAX_CYCLE_IMAGES):
    """
    return a list of image links to pass to the cycle template
    """
    return {
            'image_links': image_aref_list(max_cycle_images),
            }
        
