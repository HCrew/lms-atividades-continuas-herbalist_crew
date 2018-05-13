from django.db import models
from .aluno import Aluno
from .coordenador import Coordenador
from curriculo.models.disciplinaOfertada import DisciplinaOfertada

# Acho que ta faltando algo ali no id_disciplina_ofertada_solicitacao_matricula, não devia ter um relacionamento com a disciplina ofertada?


class SolicitacaoMatricula(models.Model):
    id_solicitacao_matricula = models.AutoField(primary_key=True)
    id_aluno_solicitacao_matricula = models.ForeignKey(
        Aluno, models.DO_NOTHING, db_column='id_aluno_solicitacao_matricula'
    )
    id_disciplina_ofertada_solicitacao_matricula = models.ForeignKey(
        DisciplinaOfertada, models.DO_NOTHING, db_column='id_disciplina_ofertada_solicitacao_matricula'
    )
    dt_solicitacao_solicitacao_matricula = models.DateField()
    id_coordenador_solicitacao_matricula = models.ForeignKey(
        Coordenador, models.DO_NOTHING, db_column='id_coordenador_solicitacao_matricula', blank=True, null=True
    )
    status_solicitacao_matricula = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_solicitacao_matricula'