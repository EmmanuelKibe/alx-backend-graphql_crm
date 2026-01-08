import django_filters
from .models import Customer, Product, Order
from django.db.models import Q

class CustomerFilter(django_filters.FilterSet):
    # Case-insensitive partial matches
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    
    # Custom filter for phone pattern (Challenge)
    phone_pattern = django_filters.CharFilter(method='filter_phone_pattern')

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def filter_phone_pattern(self, queryset, name, value):
        # Matches customers whose phone starts with the provided value (e.g., +1)
        return queryset.filter(phone_number__startswith=value)

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    # Filtering products with low stock (Think)
    stock_lte = django_filters.NumberFilter(field_name='stock', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']

class OrderFilter(django_filters.FilterSet):
    # Related field lookups
    customer_name = django_filters.CharFilter(method='filter_by_customer_name')
    product_name = django_filters.CharFilter(field_name='product__name', lookup_expr='icontains')
    
    order_date_gte = django_filters.DateTimeFilter(field_name='order_date', lookup_expr='gte')
    order_date_lte = django_filters.DateTimeFilter(field_name='order_date', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['quantity', 'order_date']

    def filter_by_customer_name(self, queryset, name, value):
        # Searches both first and last name
        return queryset.filter(
            Q(customer__first_name__icontains=value) | 
            Q(customer__last_name__icontains=value)
        )