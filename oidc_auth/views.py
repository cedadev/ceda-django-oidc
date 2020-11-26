""" App views module. """

__author__ = "William Tucker"
__date__ = "2020-11-25"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from mozilla_django_oidc.utils import import_from_settings
from mozilla_django_oidc.views import OIDCLogoutView


def logout(request):

    logout_endpoint = import_from_settings("OIDC_OP_LOGOUT_ENDPOINT", "")
    return logout_endpoint + "?redirect_uri=" + request.build_absolute_uri("/")
