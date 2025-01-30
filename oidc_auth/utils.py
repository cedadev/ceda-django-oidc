""" App utility functions. """

__author__ = "William Tucker"
__date__ = "2020-11-27"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


import requests

from django.conf import settings
from mozilla_django_oidc.utils import import_from_settings \
    as _import_from_settings


# Map of mozilla-django-oidc settings to OIDC metadata endpoint keys
_SERVER_ENDPOINT_MAP = {
    "OIDC_OP_JWKS_ENDPOINT": "jwks_uri",
    "OIDC_OP_AUTHORIZATION_ENDPOINT": "authorization_endpoint",
    "OIDC_OP_LOGOUT_ENDPOINT": "end_session_endpoint",
    "OIDC_OP_TOKEN_ENDPOINT": "token_endpoint",
    "OIDC_OP_USER_ENDPOINT": "userinfo_endpoint",
}


def _fetch_server_metadata(endpoint):
    """ Unused function to fetch metadata from an OIDC server's well-known
    endpoint.
    """

    data = requests.get(endpoint)
    return data.json()


def import_from_settings(attr, *args):
    """ Unused function to map mozilla-django-oidc settings to pre-fetched
    OIDC server metadata.
    """

    # This should be cached
    metadata = _fetch_server_metadata(settings.OIDC_METADATA_ENDPOINT)
    if attr in _SERVER_ENDPOINT_MAP:
        return metadata[_SERVER_ENDPOINT_MAP[attr]]

    return _import_from_settings(attr, *args)


def _build_redirect_url(request):

    redirect_url = getattr(settings, "LOGOUT_REDIRECT_URL", None)
    if not redirect_url:
        redirect_url = request.GET.get("next", "/")
    return request.build_absolute_uri(redirect_url)


def generate_logout_url(request):
    """ Builds a logout URL with redirect URI.
    Requires setting the OIDC_OP_LOGOUT_ENDPOINT
    """

    logout_endpoint = getattr(settings, "OIDC_OP_LOGOUT_ENDPOINT", "")

    return f"{logout_endpoint}?redirect_uri={_build_redirect_url(request)}"


def generate_id_token_logout_url(request):
    """ Builds a logout URL with redirect URI.
    Requires setting the OIDC_OP_LOGOUT_ENDPOINT
    """

    logout_endpoint = getattr(settings, "OIDC_OP_LOGOUT_ENDPOINT", "")
    oidc_id_token = request.session["oidc_id_token"]

    url = (f"{logout_endpoint}"
        f"?post_logout_redirect_uri={_build_redirect_url(request)}"
        f"&id_token_hint={oidc_id_token}"
    )
    return url
