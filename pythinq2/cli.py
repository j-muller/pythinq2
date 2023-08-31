"""A CLI tool to control your LG devices.

Usage:
  pythinq2 authenticate <username> <password> [--country <country>] [--language <language>]
"""  # noqa: E501
import logging

from docopt import docopt
from tabulate import tabulate

from pythinq2 import __version__, ThinqAPI

LOGGER = logging.getLogger(__name__)


def authenticate(username, password, country="US", language="en-US"):
    """Authenticate user and get token from LG API."""
    LOGGER.info("Authentication as: %s", username)

    api = ThinqAPI(
        username=username,
        password=password,
        country_code=country,
        language=language,
    )
    token = api.authenticate()

    print(
        tabulate(
            [
                ["Access Token", token["access_token"]],
                ["Refresh Token", token["refresh_token"]],
            ],
            tablefmt="fancy_grid",
        ),
    )


def main():
    """Entry point."""
    args = docopt(__doc__, version=__version__)

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    if args["authenticate"]:
        authenticate(
            username=args["<username>"],
            password=args["<password>"],
            country=args["<country>"],
            language=args["<language>"],
        )


if __name__ == "__main__":
    main()
