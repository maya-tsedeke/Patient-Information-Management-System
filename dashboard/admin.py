

# Register your models here.
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth.models import User
from .views import dashboard

class CustomAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['dashboard_url'] = reverse('dashboard')
        return context

    def index(self, request, extra_context=None):
        # Call the superclass index view to get the standard index page
        response = super().index(request, extra_context=extra_context)

        # Add a link to the dashboard page
        dashboard_link = format_html('<li><a href="{}">Dashboard</a></li>', reverse('dashboard'))
        response.content = response.content.replace(b'</ul>\n', dashboard_link.encode('utf-8') + b'</ul>\n')

        return response

custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(User)