# Generated by Django 5.2.3 on 2025-06-14 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0005_remove_tarefaeap_titulo_alter_tarefaeap_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardkanban',
            name='descricao',
        ),
        migrations.AddField(
            model_name='cardkanban',
            name='responsaveis',
            field=models.ManyToManyField(related_name='tarefas', to='gerencia.funcionario'),
        ),
        migrations.DeleteModel(
            name='TarefaEAP',
        ),
    ]
