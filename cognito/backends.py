from django.contrib.auth.models import User


from django.contrib.auth import login, logout

from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        username = request.GET.get("username", "shubham")
        user = User.objects.filter(username=username)
        if user:
            login(request, user[0])
