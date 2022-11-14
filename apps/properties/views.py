import logging
import django_filters

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,generics,permissions,status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
# pems
from .exceptions import PropertyNotFound
from .models import Property,PropertyViews
from .pagination import PropertyPagination
from .serializers import (
    PropertySerializer,PropertyCreateSerializer,PropertyViewSerializer
)

logger = logging.getLogger(__name__)

class PropertyFilter(django_filters.FilterSet):
    advert_type = django_filters.ChoiceFilter(field_name="advert_type",lookup_expr="iexact")