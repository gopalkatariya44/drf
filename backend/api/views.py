from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "hi i am gopal creating an api in django!"})
