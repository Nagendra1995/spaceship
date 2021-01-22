from django.conf.urls import url

from api.views import AddSpaceship, Addlocation

urlpatterns = [
    url(r'^AddSpaceship', AddSpaceship, name='AddSpaceship'),
    url(r'^Addlocation', Addlocation, name='Addlocation'),

]
