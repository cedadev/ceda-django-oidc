""" Module for Django app middleware classes. """

__author__ = "William Tucker"
__date__ = "2020-11-26"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from mozilla_django_oidc.middleware import SessionRefresh as BaseSessionRefresh

from .utils import import_from_settings


class SessionRefresh(BaseSessionRefresh):
    """ Refreshes the session with the OIDC RP after expiry seconds.

    For users authenticated with the OIDC RP, verify tokens are still valid and
    if not, force the user to re-authenticate silently.
    """

    @staticmethod
    def get_settings(attr, *args):
        return import_from_settings(attr, *args)
