from django.db import models


class SchemaData(models.Model):
    """Schema data"""
    SEPARATORS = [
        ('1', 'Comma (,)'),
        ('2', 'Colon (;)')
    ]
    STRING_CHARACTER = [
        ('1', 'Double-quote (")'),
        ('2', "Quote (')")
    ]
    name = models.CharField(max_length=128)
    column_separator = models.CharField(choices=SEPARATORS, default=1, max_length=50)
    string_character = models.CharField(choices=STRING_CHARACTER, default=1, max_length=50)
    modified = models.DateField(auto_now=True)


class SchemaColumn(models.Model):
    """Schema columns"""
    TYPES = [
        ('1', 'Job'),
        ('2', 'Domain name'),
        ('3', 'Phone Number'),
        ('4', 'Company'),
        ('5', 'Integer'),
    ]
    name = models.CharField(max_length=128)
    schema = models.ForeignKey('SchemaData', related_name='columns', on_delete=models.CASCADE)
    type = models.CharField(choices=TYPES, default=1, max_length=25)
    extra_data_type = models.CharField(max_length=1024, blank=True)


class SchemaSet(models.Model):
    STATUS = [
        ('1', 'Processing'),
        ('2', 'Ready')
    ]
    schema = models.ForeignKey(SchemaData, related_name='sets', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=15)
    link_download = models.CharField(max_length=248, blank=True)
