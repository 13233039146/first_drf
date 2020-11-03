from django_filters.rest_framework import FilterSet

from token_app.models import Phone



class PhoneFilter(FilterSet):
    from django_filters import filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        model = Phone
        fields = ["brand", "min_price", "max_price"]
