from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

class Atendimento(models.Model):
    SERVICO_CHOICES = (
        ('limpeza simples', 'limpeza simples'),
        ('limpeza profunda', 'limpeza profunda'),
    )

    servico = models.CharField(max_length=20, choices=SERVICO_CHOICES)
    atendente = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'groups__name': 'atendentes'}, related_name='atendimentos_criados')
    helper = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'groups__name': 'helpers'}, related_name='atendimentos_executados')
    preco = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='Não necessita preencher')

    FORMA_CHOICES = (
        ('Espécie', 'Espécie'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('PIX', 'PIX'),
        ('Cheque', 'Cheque'),
    )
    forma_de_pagamento = models.CharField(max_length=20, choices=FORMA_CHOICES)
    data_de_cadastro = models.DateTimeField(default=timezone.now)
    data_do_servico = models.DateTimeField(default=timezone.now)
    
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Realizado', 'Realizado'),
        ('Cancelado', 'Cancelado'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    nome_do_cliente = models.TextField(max_length=100, blank=False)
    telefone_do_cliente = models.TextField(max_length=14, blank=False)
    endereço_do_cliente = models.TextField(max_length=200, blank=False)
    def save(self, *args, **kwargs):
        if self.servico == 'limpeza simples':
            self.preco = 100.00
        elif self.servico == 'limpeza profunda':
            self.preco = 250.00
        super(Atendimento, self).save(*args, **kwargs)

    def __str__(self):
        return f"Atendimento de {self.servico} com preço de {self.preco} criado por {self.atendente.username} e executado por {self.helper.username} em {self.data_de_cadastro}"