from django import template

register = template.Library()

@register.simple_tag
def user_reacted(user, post):
    return post.post_reactions.filter(user=user).count() > 0

@register.simple_tag
def user_follows(user, following):
    return following in user.following.all()

@register.inclusion_tag('network/like_btn.html')
def like_btn(user, post):
    context = {
        'u': user, 
        'post': post, 
        'reacted': False, 
        'type': None}
    if user.is_authenticated:
        reaction = post.post_reactions.filter(user=user).first()
        context['reacted'] = True if reaction else False
        context['type'] = reaction.type if reaction else None
    return context
