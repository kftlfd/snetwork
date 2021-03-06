from django import template

register = template.Library()

@register.simple_tag
def user_reacted(user, post):
    return post.post_reactions.filter(user=user).count() > 0

@register.simple_tag
def user_follows(user, following):
    return following in user.following.all()

@register.inclusion_tag('network/likebtn.html')
def likebtn(user, post):
    context = {
        'u': user, 
        'post': post, 
        'reacted': False}
    if user.is_authenticated:
        reaction = post.post_reactions.filter(user=user).first()
        context['reacted'] = True if reaction else False
    return context
