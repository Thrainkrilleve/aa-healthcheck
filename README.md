# AA Healthcheck

[![Badge: Version]][pypi]
[![Badge: License]][license]
[![Badge: Supported Python Versions]][pypi]
[![Badge: Supported Django Versions]][pypi]
![Badge: pre-commit]
[![Badge: pre-commit.ci status]][pre-commit.ci status]
[![Badge: Code Style: black]][black code formatter documentation]
[![Badge: Automated Tests]][automated tests on github]
[![Badge: Code Coverage]][codecov]

A healthcheck/heartbeat app for [Alliance Auth]

## Features

Ping healthcheck.io every 5 minutes, which will alert when a ping isn't received.

### Future Features

- uptime kuma support

## Installation

- healthcheck is a plugin for Alliance Auth. If you don't have Alliance Auth running
  already, please install it first before proceeding. (see the official
  [Alliance Auth installation guide] for details)

```bash
pip install aa-healthcheck
```

- Create a healthcheck.io account and associated check, copy the given ping URL

Configure your Auth settings (`local.py`) as follows:

- Add `'healthcheck'` to `INSTALLED_APPS`
- Add the following lines to your settings file:

```python
HEALTHCHECK_URL = "https://hc-ping.com/"  # Replace with your healthchek.io url
if "healthcheck" in INSTALLED_APPS:
    # Run every 5 minutes
    CELERYBEAT_SCHEDULE["Healthcheck :: Heartbeat"] = {
        "task": "skyhooks.tasks.update_skyhooks",
        "schedule": crontab(minute="*/5"),
    }
```

There are curently no migrations or static files

- Restart your supervisor services for Auth

<!-- Links -->

[alliance auth]: https://gitlab.com/allianceauth/allianceauth "Alliance Auth"
[alliance auth installation guide]: https://allianceauth.readthedocs.io/en/latest/installation/allianceauth.html "Alliance Auth installation guide"
[automated tests on github]: https://github.com/astrum-mechanica/aa-healthcheck/actions/workflows/automated-checks.yml
[badge: automated tests]: https://github.com/astrum-mechanica/aa-healthcheck/actions/workflows/automated-checks.yml/badge.svg "Automated Tests"
[badge: code coverage]: https://codecov.io/gh/astrum-mechanica/aa-healthcheck/branch/master/graph/badge.svg "Code Coverage"
[badge: code style: black]: https://img.shields.io/badge/code%20style-black-000000.svg "Code Style: black"
[badge: license]: https://img.shields.io/github/license/astrum-mechanica/aa-healthcheck "License"
[badge: pre-commit]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white "pre-commit"
[badge: pre-commit.ci status]: https://results.pre-commit.ci/badge/github/astrum-mechanica/aa-healthcheck/master.svg "pre-commit.ci status"
[badge: supported django versions]: https://img.shields.io/pypi/djversions/aa-healthcheck?label=django "Supported Django Versions"
[badge: supported python versions]: https://img.shields.io/pypi/pyversions/aa-healthcheck "Supported Python Versions"
[badge: version]: https://img.shields.io/pypi/v/aa-healthcheck?label=release "Version"
[black code formatter documentation]: http://black.readthedocs.io/en/latest/
[codecov]: https://codecov.io/gh/astrum-mechanica/aa-healthcheck
[license]: https://github.com/astrum-mechanica/aa-healthcheck/blob/master/LICENSE
[pre-commit.ci status]: https://results.pre-commit.ci/latest/github/astrum-mechanica/aa-healthcheck/master "pre-commit.ci"
[pypi]: https://pypi.org/project/aa-healthcheck/
