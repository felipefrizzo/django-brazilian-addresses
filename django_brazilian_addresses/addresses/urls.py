from rest_framework import routers

from django_brazilian_addresses.addresses.views import CountryView, \
    StateView, CityView, NeighborhoodView, StreetView

router = routers.SimpleRouter()
router.register(r'countries', CountryView)
router.register(r'states', StateView)
router.register(r'cities', CityView)
router.register(r'neighborhoods', NeighborhoodView)
router.register(r'streets', StreetView)

urlpatterns = router.urls
