from django.db import models


class SchemaData(models.Model):
    """Schema data"""
    SEPARATORS = [
        (1, 'Comma (,)'),
        (2, 'Colon (;)')
    ]
    STRING_CHARACTER = [
        (1, 'Double-quote (")'),
        (2, "Quote (')")
    ]
    name = models.CharField(max_length=128)
    column_separator = models.CharField(choices=SEPARATORS, default=1)
    string_character = models.CharField(choices=STRING_CHARACTER, default=1)


class SchemaColumns(models.Model):
    """Schema columns"""
    TYPES = [
        (1, 'Job'),
        (2, 'Domain name'),
        (3, 'Phone Number'),
        (4, 'Company'),
        (5, 'Integer'),
    ]
    name = models.CharField(max_length=128)
    schema = models.ForeignKey('SchemaData', related_name='columns', on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, default=1)
