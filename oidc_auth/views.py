""" App views module. """

__author__ = "William Tucker"
__date__ = "2020-11-25"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from django.contrib import auth
from django.http import HttpResponseRedirect
from mozilla_django_oidc.views import OIDCLogoutView as BaseOIDCLogoutView
from mozilla_django_oidc.views import OIDCAuthenticationRequestView

from .utils import import_from_settings


class OIDCLoginView(OIDCAuthenticationRequestView):
    """ OIDC client authentication HTTP endpoint. """

    @staticmethod
    def get_settings(attr, *args):
        return import_from_settings(attr, *args)


class OIDCLogoutView(BaseOIDCLogoutView):
    """ OIDC logout helper view. """

    @staticmethod
    def get_settings(attr, *args):
        return import_from_settings(attr, *args)

    def post(self, request):
        """ Log out the user. """
        logout_url = self.redirect_url

        if request.user.is_authenticated:

            # Build a logout URL with redirect from the OP endpoint
            logout_endpoint = self.get_settings("OIDC_OP_LOGOUT_ENDPOINT", "")
            logout_url = logout_endpoint + \
                "?redirect_uri=" + request.build_absolute_uri("/")

            # Log out the Django user if they were logged in.
            auth.logout(request)

        return HttpResponseRedirect(logout_url)


class GetOIDCLogoutView(OIDCLogoutView):
    """ OIDC logout helper view supporting GET method logout. """

    def get(self, request):
        return self.post(request)
