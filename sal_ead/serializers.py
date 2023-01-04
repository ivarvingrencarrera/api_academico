from sal_ead.models import Oferta
from rest_framework import serializers
from django.utils import timezone
from .validators import *
import json


class AccountSerializer(serializers.ModelSerializer):
    origin = serializers.SerializerMethodField()
    course_type = serializers.SerializerMethodField()
    offer_id = serializers.SerializerMethodField()
    first_level_name = serializers.SerializerMethodField()
    first_level_sis_account_id = serializers.SerializerMethodField()
    second_level_name = serializers.SerializerMethodField()
    second_level_sis_account_id = serializers.SerializerMethodField()
    third_level_name = serializers.SerializerMethodField()
    third_level_sis_account_id = serializers.SerializerMethodField()
    fourth_level_sis_parent_account_id = serializers.SerializerMethodField()

    class Meta:
        model = Oferta
        fields = ['origin', 'course_type', 'offer_id', 'first_level_name', 'first_level_sis_account_id', 'second_level_name',
                  'second_level_sis_account_id', 'third_level_name', 'third_level_sis_account_id',
                  'fourth_level_sis_parent_account_id']

    def get_origin(self, obj) -> str:
        return 'SAL_EAD'

    def get_offer_id(self, obj) -> int:
        return obj.seq_oferta

    def get_first_level_name(self, obj) -> str:
        if obj.cod_tipo_curso == 1:
            account_name = f"{obj.nom_curso} - {obj.dat_inicio.strftime('%Y')}"
        elif obj.cod_tipo_curso == 8:
            account_name = (
                f"{obj.nom_curso.replace(' - CD', '')} - Oferta {str(obj.num_oferta).zfill(2)}"
            )
        else:
            account_name = f"{obj.nom_curso} - Oferta {str(obj.num_oferta).zfill(2)}"
        return account_name

    def get_first_level_sis_account_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            account_sis_account_id = f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_curso}_{obj.num_oferta}"
        else:
            account_sis_account_id = (
                f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_instituto}_{obj.cod_curso}_{obj.num_oferta}"
            )
        return account_sis_account_id

    def get_second_level_name(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            account_name = f"{obj.nom_curso.replace(' - CD', '')}"
        else:
            account_name = obj.nom_curso
        return account_name

    def get_second_level_sis_account_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            account_sis_account_id = f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_curso}"
        else:
            account_sis_account_id = f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_instituto}_{obj.cod_curso}"
        return account_sis_account_id

    def get_third_level_name(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            name = "Curso/Disciplina"
        else:
            name = obj.nome_instituto
        return name

    def get_third_level_sis_account_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            sis_account_id = "SALEAD_8"
        else:
            sis_account_id = f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_instituto}"
        return sis_account_id

    def get_fourth_level_sis_parent_account_id(self, obj):
        if obj.cod_tipo_curso == 8:
            sis_account_id = "SALEAD_1"
        else:
            sis_account_id = f"SALEAD_{obj.cod_tipo_curso}"
        return sis_account_id

    def get_course_type(self, obj):
        course_type = ''
        match obj.cod_tipo_curso:
            case 1:
                course_type = f'Especialização {obj.origem}'
            case 2:
                course_type = 'Desconhecido'
            case 3:
                course_type = 'Desconhecido'
            case 5:
                course_type = f'Aperfeiçoamento {obj.origem}'
            case 6:
                course_type = 'Desconhecido'
            case 7:
                course_type = 'Curta duração'
            case 8:
                course_type = 'Núcleo Comum'
            case 9:
                course_type = 'Desconhecido'
        return course_type
