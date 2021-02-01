from django.urls import path

from schemas.views import CreateSchemaView, SchemasView, SchemasDeleteView, SchemaSetsView

urlpatterns = [
    path('create/', CreateSchemaView.as_view(), name='create_schema'),
    path('', SchemasView.as_view(), name='schemas'),
    path('delete/<int:pk>/', SchemasDeleteView.as_view(), name='delete_schema'),
    path('datasets/<int:pk>/', SchemaSetsView.as_view(), name='schema_sets')
]
