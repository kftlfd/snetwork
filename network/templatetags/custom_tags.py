from django import template

register = template.Library()

@register.simple_tag
def user_reacted(user, post):
    return post.post_reactions.filter(user=user).count() > 0
