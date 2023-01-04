from django.db import models
from django.utils import timezone

class Oferta(models.Model):
    seq_chave_oferta = models.IntegerField(primary_key=True)
    seq_oferta = models.IntegerField(blank=True, null=True)
    nom_curso = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cod_curso = models.IntegerField(blank=True, null=True)
    cod_curso_ead = models.CharField(db_column='cod_curso_EAD', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_curso = models.SmallIntegerField(blank=True, null=True)
    num_oferta = models.IntegerField(blank=True, null=True)
    num_vagas = models.SmallIntegerField(blank=True, null=True)
    val_oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    qte_carga_horaria = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dat_inicio = models.DateTimeField(blank=True, null=True)
    dat_fim = models.DateTimeField(blank=True, null=True)
    dat_resultado_selecao = models.DateTimeField(blank=True, null=True)
    dat_inicio_matricula = models.DateTimeField(blank=True, null=True)
    dat_fim_matricula = models.DateTimeField(blank=True, null=True)
    dat_inclusao = models.DateTimeField(blank=True, null=True)
    dat_cancelamento = models.DateTimeField(blank=True, null=True)
    ind_atualizado_ead = models.BooleanField(db_column='ind_atualizado_EAD', blank=True, null=True)  # Field name made lowercase.
    dat_atualizacao_ead = models.DateTimeField(db_column='dat_atualizacao_EAD', blank=True, null=True)  # Field name made lowercase.
    ind_atualizado_sal = models.BooleanField(db_column='ind_atualizado_SAL', blank=True, null=True)  # Field name made lowercase.
    dat_atualizacao_sal = models.DateTimeField(db_column='dat_atualizacao_SAL', blank=True, null=True)  # Field name made lowercase.
    ind_pagto_puc = models.SmallIntegerField(db_column='ind_pagto_PUC', blank=True, null=True)  # Field name made lowercase.
    idt_inscricao_online = models.SmallIntegerField(blank=True, null=True)
    ind_selecao_automatica = models.BooleanField(blank=True, null=True)
    ind_excluido = models.BooleanField(blank=True, null=True)
    lms_account_id = models.IntegerField(blank=True, null=True)
    origem = models.CharField(max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    nome_instituto = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cod_instituto = models.IntegerField(blank=True, null=True)
    dat_fim_acesso = models.DateTimeField(blank=True, null=True)
    ind_espaco_compartilhado = models.BooleanField(blank=True, null=True)
    dsc_espaco_compartilhado = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    seq_localizacao = models.IntegerField(blank=True, null=True)
    dsc_localizacao = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    qtd_turma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oferta'