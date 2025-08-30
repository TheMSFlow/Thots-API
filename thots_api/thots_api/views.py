from django.http import HttpResponse
from django.urls import reverse

def home(request):
    links = [
        ("Admin", reverse("admin:index")),
        ("API Root", "/api/"),
        ("Register", "/api/register/"),
        ("Login", "/api/login/"),
        ("Logout", "/api/logout/"),
        ("Current User", "/api/me/"),
    ]

    html = "<h1>Welcome to Thots API 🚀</h1><ul>"
    for name, url in links:
        html += f'<li><a href="{url}">{name}</a></li>'
    html += "</ul>"

    return HttpResponse(html)
