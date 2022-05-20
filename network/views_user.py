from django.shortcuts import render


def user_view(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, "network/user.html", {'user': user})
