from sal_ead.models import Oferta
from sal_ead.serializers import AccountUnsyncSerializer, CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.db.models import Q


class AccountUnsyncViewSet(viewsets.ModelViewSet):

    queryset = Oferta.objects.filter(
        origem='EAD', dat_inicio__gt='2023-01-01 00:00:00', ind_excluido=0, dat_cancelamento=None)
    serializer_class = AccountUnsyncSerializer

