# recipes/templatetags/custom_tags.py

import random
from django import template

register = template.Library()


@register.simple_tag
def random_background(num_images):
    return random.randint(1, num_images - 1)
