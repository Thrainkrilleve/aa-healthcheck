"""Tasks."""

# Third Party
import requests
from celery import shared_task

# Alliance Auth
from allianceauth.services.hooks import get_extension_logger

from .app_settings import HEALTHCHECK_URL

logger = get_extension_logger(__name__)


@shared_task
def heartbeat():
    if not HEALTHCHECK_URL:
        logger.debug("HEALTHCHECK_URL is not set. Skipping heartbeat.")
        return

    try:
        requests.get(HEALTHCHECK_URL, timeout=10)
    except requests.RequestException:
        logger.warning("Healthchecks.io ping failed", exc_info=True)
