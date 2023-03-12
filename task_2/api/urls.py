from django.urls import path
from api.views import test

urlpatterns = [
    path('v1/vendor-code', test)
]
