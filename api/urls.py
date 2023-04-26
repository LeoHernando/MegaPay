from django.urls import include, path

from rest_framework import routers

from api.views import EmployeesViewSet, PayoutsViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'payouts', PayoutsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]