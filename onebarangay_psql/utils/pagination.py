"""Custom pagination for onebarangay_psql."""
from rest_framework.pagination import PageNumberPagination


class PageNumberWithPageSizePagination(PageNumberPagination):
    """Pagination class that allows for custom page size."""

    page_size_query_param = "page_size"
