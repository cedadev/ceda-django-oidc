""" App utility functions. """

__author__ = "William Tucker"
__date__ = "2020-11-27"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


import requests

from django.conf import settings
from mozilla_django_oidc.utils import import_from_settings \
    as _import_from_settings


_SERVER_ENDPOINT_MAP = {
    "OIDC_OP_JWKS_ENDPOINT": "jwks_uri",
    "OIDC_OP_AUTHORIZATION_ENDPOINT": "authorization_endpoint",
    "OIDC_OP_LOGOUT_ENDPOINT": "end_session_endpoint",
    "OIDC_OP_TOKEN_ENDPOINT": "token_endpoint",
    "OIDC_OP_USER_ENDPOINT": "userinfo_endpoint",
}


def _fetch_server_metadata(endpoint):

    data = requests.get(endpoint)
    return data.json()

_server_metadata = _fetch_server_metadata(settings.OIDC_METADATA_ENDPOINT)


def import_from_settings(attr, *args):

    if attr in _SERVER_ENDPOINT_MAP:
        return _server_metadata[_SERVER_ENDPOINT_MAP[attr]]

    return _import_from_settings(attr, *args)
