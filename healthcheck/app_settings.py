"""App settings."""

# Django
from django.conf import settings

HEALTHCHECK_URL = getattr(settings, "HEALTHCHECK_URL", None)
