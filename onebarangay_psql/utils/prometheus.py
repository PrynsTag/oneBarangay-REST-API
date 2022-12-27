"""Util for getting the prometheus metrics."""
from prometheus_client import CollectorRegistry, Counter, Histogram, generate_latest


registry = CollectorRegistry()

PROM_GRAPHQL_REQUEST_TIME = Histogram(
    "request_processing_seconds",
    "Time spent processing an API request",
    registry=registry,
)

PROM_PAGEVIEWS = Counter(
    "pageviews",
    "Number of pageviews",
    registry=registry,
)


def registry_to_text():
    """Return the prometheus metrics as text."""
    return generate_latest(registry)
