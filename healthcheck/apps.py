"""App configuration"""

# Django
from django.apps import AppConfig
from django.utils.text import format_lazy

# aa healthcheck
from healthcheck import __title_translated__, __version__


class HealthCheckConfig(AppConfig):
    """App config"""

    name = "healthcheck"
    label = "healthcheck"
    verbose_name = format_lazy(
        "{app_title} v{version}", app_title=__title_translated__, version=__version__
    )
