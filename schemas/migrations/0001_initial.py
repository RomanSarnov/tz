# Generated by Django 3.0.4 on 2021-01-31 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchemaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('column_separator', models.CharField(choices=[(1, 'Comma (,)'), (2, 'Colon (;)')], default=1, max_length=50)),
                ('string_character', models.CharField(choices=[(1, 'Double-quote (")'), (2, "Quote (')")], default=1, max_length=50)),
                ('modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[(1, 'Processing'), (2, 'Ready')], max_length=15)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sets', to='schemas.SchemaData')),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[(1, 'Job'), (2, 'Domain name'), (3, 'Phone Number'), (4, 'Company'), (5, 'Integer')], default=1, max_length=25)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='schemas.SchemaData')),
            ],
        ),
    ]
