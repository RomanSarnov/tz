from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from schemas.models import SchemaColumn, SchemaSet, SchemaData


class CreateSchemaView(LoginRequiredMixin, View):
    """Schemas list"""

    def get(self, request):
        return render(request, 'schema/add-schemas.html', context={})


class SchemasView(LoginRequiredMixin, View):
    """Schemas list"""

    def get(self, request):
        schemas = SchemaData.objects.all()
        for i in schemas:
            print(i.modified)
        return render(request, 'schema/schemas.html', context={'schemas': schemas})


class SchemasDeleteView(LoginRequiredMixin, View):
    def get(self, requests, pk):
        schema = SchemaData.objects.get(pk=pk)
        schema.delete()
        return redirect('schemas')


class SchemaSetsView(LoginRequiredMixin, View):
    def get(self, requests, pk):
        schema = SchemaData.objects.prefetch_related('sets').get(pk=pk)
        return render(requests, 'schema/data-sets.html', context={'schema': schema})
