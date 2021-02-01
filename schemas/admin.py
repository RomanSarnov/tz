from django.contrib import admin
from schemas.models import SchemaData, SchemaColumn, SchemaSet

admin.site.register(SchemaSet)
admin.site.register(SchemaColumn)
admin.site.register(SchemaData)

