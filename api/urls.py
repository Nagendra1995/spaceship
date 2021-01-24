from django.conf.urls import url

from api.views import AddSpaceship, Addlocation, DelSpaceship, DelLocation, UpdateStatus, Travel

urlpatterns = [
    url(r'^AddSpaceship', AddSpaceship, name='AddSpaceship'),
    url(r'^Addlocation', Addlocation, name='Addlocation'),
    url(r'^DelLocation', DelLocation, name='DelLocation'),
    url(r'^DelSpaceship', DelSpaceship, name='DelSpaceship'),
    url(r'^UpdateStatus', UpdateStatus, name='UpdateStatus'),
    url(r'^Travel', Travel, name='Travel'),

]
