from django import template
register = template.Library()

@register.simple_tag
def to_rating(rating: int):
    emotes = ('fa-angry','fa-frown','fa-meh','fa-smile','fa-laugh')
    # return ['fa-meh-blank'] * 5 if rating <= 0 else [emotes[rating-1]] * 5
    return [emotes[rating-1]] * rating