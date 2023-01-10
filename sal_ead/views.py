from sal_ead.models import Oferta
from sal_ead.serializers import AccountUnsyncSerializer, CourseSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.db.models import Q


class AccountUnsyncViewSet(viewsets.ModelViewSet):

    queryset = Oferta.objects.all()
    # queryset = Oferta.objects.filter(
    #     origem='EAD', dat_inicio__gt='2023-01-01 00:00:00', ind_excluido=0, dat_cancelamento=None)
    serializer_class = AccountUnsyncSerializer


    def get_queryset(self):

        query = Q()

        origem = self.request.GET.get('origem')
        if origem is not None:
            query.add(Q(origem=origem), Q.AND)

        dat_inicio = self.request.GET.get('dat_inicio')
        if dat_inicio is not None:
            query.add(Q(dat_inicio__gte=dat_inicio), Q.AND)

        ind_excluido = self.request.GET.get('ind_excluido')
        if ind_excluido is not None:
            query.add(Q(ind_excluido=ind_excluido), Q.AND)

        dat_cancelamento = self.request.query_params.get('dat_cancelamento')
        if dat_cancelamento is not None:
            query.add(Q(dat_cancelamento=dat_cancelamento), Q.AND)
        else:
            query.add(Q(dat_cancelamento=None), Q.AND)

        return Oferta.objects.filter(query)