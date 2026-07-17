from unittest.mock import patch

# Django
from django.test import TestCase

# aa healthcheck
from healthcheck.tasks import heartbeat


class TestTasks(TestCase):
    @patch("healthcheck.tasks.HEALTHCHECK_URL", "https://hc-ping.com/fake-uuid")
    @patch("healthcheck.tasks.requests.get")
    def test_should_run_task_when_configured(self, mock_get):
        # when
        heartbeat()
        
        # then
        mock_get.assert_called_once_with("https://hc-ping.com/fake-uuid", timeout=10)

    @patch("healthcheck.tasks.HEALTHCHECK_URL", None)
    @patch("healthcheck.tasks.requests.get")
    def test_should_skip_when_not_configured(self, mock_get):
        # when
        heartbeat()
        
        # then
        mock_get.assert_not_called()
