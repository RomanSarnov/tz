from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class SchemasView(LoginRequiredMixin, View):
    """Schemas list"""

    def get(self, request):
        return render(request, 'schema/add-schemas.html', context={})


class SchemView(View):
    """Schemas list"""

    def get(self, request):
        return render(request, 'schema/schemas.html', context={})
