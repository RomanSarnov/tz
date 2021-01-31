from django.urls import path

from schemas.views import SchemasView, SchemView

urlpatterns = [
    path('', SchemasView.as_view(), name='schemas'),
    path('add-column/', SchemasView.as_view(), name='add_column'),
    path('views/', SchemView.as_view(), name='views'),

]
