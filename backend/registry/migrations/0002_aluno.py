# Generated by Django 5.2.2 on 2025-06-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0, null=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]
