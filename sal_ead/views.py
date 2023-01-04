from sal_ead.models import Oferta
from sal_ead.serializers import AccountSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.db.models import Q


class AccountUnsyncViewSet(viewsets.ModelViewSet):

    queryset = Oferta.objects.filter()
    serializer_class = AccountSerializer
