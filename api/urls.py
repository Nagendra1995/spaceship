from django.conf.urls import url

from api.views import AddSpaceship

urlpatterns = [
    url(r'^AddSpaceship', AddSpaceship, name='AddSpaceship')

]
