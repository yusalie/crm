import django_filters
from .models import*
from django_filters import DateFilter

class OrderFilter(django_filters.FilterSet):
    class Meta:
        start_date = DateFilter
        model = order
        fields = '__all__'
        exclude = ['customer','date_created']
