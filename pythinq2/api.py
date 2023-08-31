import logging

from pythinq2.gateway import Gateway
from pythinq2.auth import ThinqAuth

LOGGER = logging.getLogger(__name__)


class ThinqAPI:
    def __init__(
        self, username, password, language="en-US", country_code="US"
    ):
        """Create a new API object."""
        self.username = username
        self.password = password
        self.language = language
        self.country_code = country_code

        self._gateway = None
        self._auth = None

    def authenticate(self):
        """Authenticate an user on LG API."""
        if self._gateway is None:
            self._gateway = Gateway(
                country_code=self.country_code,
                language=self.language,
            )

        self._auth = ThinqAuth(self._gateway)
        return self._auth.login(self.username, self.password)
