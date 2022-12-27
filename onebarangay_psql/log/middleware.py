"""Page Views and Time Spent custom middleware for Prometheus."""
import time

from onebarangay_psql.utils.prometheus import PROM_GRAPHQL_REQUEST_TIME, PROM_PAGEVIEWS


class PageViewsMiddleware:
    """Middleware for counting page views."""

    def __init__(self, get_response):
        """Initialize the middleware."""
        self.get_response = get_response

    def __call__(self, request):
        """Is called once per request."""
        response = self.get_response(request)

        PROM_PAGEVIEWS.inc()

        return response


class TimeSpentMiddleware:
    """Middleware for measuring time spent."""

    def __init__(self, get_response):
        """Initialize the middleware."""
        self.get_response = get_response

    def __call__(self, request):
        """Is called once per request."""
        response = self.get_response(request)
        return response

    # pylint: disable=unused-argument
    def process_view(self, request, view_func, view_args, view_kwargs):
        """Is called just before Django calls the view."""
        request.start_time = time.time()

    def process_response(self, request, response):
        """Is called just before Django returns the response to the browser."""
        response_time = time.time() - request.start_time
        PROM_GRAPHQL_REQUEST_TIME.observe(response_time)
        return response
