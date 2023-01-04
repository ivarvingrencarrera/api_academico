from django.contrib import admin
from django.urls import path, include
from sal_ead.models import Oferta
from sal_ead.views import AccountUnsyncViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', AccountUnsyncViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
