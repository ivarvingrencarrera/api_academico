from sal_ead.models import Oferta
from rest_framework import serializers
from .validators import *


class AccountUnsyncSerializer(serializers.ModelSerializer):
    origin = serializers.SerializerMethodField()
    course_type = serializers.SerializerMethodField()
    offer_id = serializers.SerializerMethodField()
    first_level = serializers.SerializerMethodField()
    second_level = serializers.SerializerMethodField()
    third_level = serializers.SerializerMethodField()

    class Meta:
        model = Oferta
        fields = ['origin', 'course_type', 'offer_id',
                  'first_level', 'second_level', 'third_level']

    def get_origin(self, obj) -> str:
        return 'SAL_EAD'

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

    def get_offer_id(self, obj) -> int:
        return obj.seq_oferta

    def get_first_level(self, obj) -> dict:
        return {
            'name': self.get_first_level_name(obj),
            'sis_account_id': self.get_first_level_sis_account_id(obj),
            'sis_parent_account_id': self.get_second_level_sis_account_id(obj)
        }

    def get_second_level(self, obj) -> dict:
        return {
            'name': self.get_second_level_name(obj),
            'sis_account_id': self.get_second_level_sis_account_id(obj),
            'sis_parent_account_id': self.get_third_level_sis_account_id(obj)
        }

    def get_third_level(self, obj) -> dict:
        return {
            'name': self.get_third_level_name(obj),
            'sis_account_id': self.get_third_level_sis_account_id(obj),
            'sis_parent_account_id': self.get_fourth_level_sis_parent_account_id(obj)
        }

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


class CourseSerializer(serializers.ModelSerializer):
    name: serializers.SerializerMethodField()
    course_code: serializers.SerializerMethodField()
    sis_course_id: serializers.SerializerMethodField()
    sis_term_id: serializers.SerializerMethodField()
    workflow_state: serializers.SerializerMethodField()
    sis_account_id: serializers.SerializerMethodField()
    section: serializers.SerializerMethodField()
    origin: serializers.SerializerMethodField()
    course_type: serializers.SerializerMethodField()
    offer_id: serializers.SerializerMethodField()
    class_id: serializers.SerializerMethodField()

    class Meta:
        model = Oferta
        fields = ['name', 'course_code', 'sis_course_id', 'sis_term_id', 'workflow_state',
                  'sis_account_id', 'section', 'origin', 'course_type', 'offer_id', 'class_id']

    def get_name(self, obj) -> str:
        discipline_index = course.discipline_index
        if obj.cod_tipo_curso == 1:
            name = (
                f"{str(discipline_index).zfill(2)} - {obj.nom_disciplina} ({obj.dat_inicio.strftime('%Y')})"
            )
        elif obj.cod_tipo_curso == 8:
            name = f"{obj.nom_disciplina.replace(' - CD', '')} - Oferta {str(obj.num_oferta).zfill(2)}"
        else:
            name = f"{obj.nom_disciplina} - Oferta {str(obj.num_oferta).zfill(2)}"
        return name

    def get_course_code(self, obj) -> str:
        discipline_index = course.discipline_index
        if obj.cod_tipo_curso == 1:
            course_code = (
                f"{str(discipline_index).zfill(2)} - {obj.nom_disciplina} ({obj.dat_inicio.strftime('%Y')})"
            )
        elif obj.cod_tipo_curso == 8:
            course_code = f"{obj.nom_disciplina.replace(' - CD', '')} - Oferta {str(obj.num_oferta).zfill(2)}"
        else:
            course_code = (
                f"{obj.nom_disciplina} - Oferta {str(obj.num_oferta).zfill(2)}"
            )
        return course_code

    def get_sis_course_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            sis_course_id = f"SALEAD_{obj.cod_curso}_{obj.num_oferta}_{obj.seq_curriculo_oferta}"
        else:
            sis_course_id = (
                f"SALEAD_{obj.cod_instituto}_{obj.cod_curso}_{obj.num_oferta}_{obj.seq_curriculo_oferta}"
            )
        return sis_course_id

    def get_sis_term_id(self, obj) -> str:
        match obj.cod_tipo_curso:
            case 1:
                sis_term_id = f"term_pos_{obj.dat_inicio.strftime('%Y')}"
            case 5:
                sis_term_id = f"term_aperfeicoamento_{obj.dat_inicio.strftime('%Y')}"
            case 7:
                sis_term_id = "term_curta_duracao"
            case 8:
                sis_term_id = f"term_curso_disciplina_{obj.dat_inicio.strftime('%Y')}"
        return sis_term_id

    def get_workflow_state(self, obj) -> str:
        return "unpublished" if obj.ind_excluido == 0 else "completed"

    def get_sis_account_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            sis_account_id = f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_curso}_{obj.num_oferta}"
        else:
            sis_account_id = (
                f"SALEAD_{obj.cod_tipo_curso}_{obj.cod_instituto}_{obj.cod_curso}_{obj.num_oferta}"
            )
        return sis_account_id

    def get_section(self, obj) -> dict:
        return {
            'name': self.get_section_name(obj),
            'sis_section_id': self.get_section_sis_section_id(obj),
            'start_at': self.get_section_start_at(obj),
            'end_at': self.get_section_end_at(obj)
        }

    def get_section_name(self, obj) -> str:
        if obj.cod_tipo_curso == 1:
            section_name = f"{obj.nom_disciplina} ({obj.dat_inicio.strftime('%Y')})"
        elif obj.cod_tipo_curso == 8:
            section_name = f"{obj.nom_disciplina.replace(' - CD', '')} - Oferta {str(obj.num_oferta).zfill(2)}"
        else:
            section_name = f"{obj.nom_disciplina} - Oferta {str(obj.num_oferta).zfill(2)}"
        return section_name

    def get_section_sis_section_id(self, obj) -> str:
        if obj.cod_tipo_curso == 8:
            section_sis_section_id = f"SALEAD_{obj.cod_curso}_{obj.num_oferta}_{obj.seq_curriculo_oferta}_section"
        else:
            section_sis_section_id = (
                f"SALEAD_{obj.cod_instituto}_{obj.cod_curso}_{obj.num_oferta}_{obj.seq_curriculo_oferta}_section"
            )
        return section_sis_section_id

    def get_section_start_at(self, obj) -> None:
        return None

    def get_section_end_at(self, obj) -> None:
        return None
