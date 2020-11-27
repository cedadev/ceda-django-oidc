""" Module for the authentication backend. """

__author__ = "William Tucker"
__date__ = "2020-09-21"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from mozilla_django_oidc.auth import OIDCAuthenticationBackend \
    as BaseOIDCAuthenticationBackend

from .utils import import_from_settings


class OIDCAuthenticationBackend(BaseOIDCAuthenticationBackend):

    @staticmethod
    def get_settings(attr, *args):
        return import_from_settings(attr, *args)

    def get_username(self, claims):

        return claims.get("preferred_username")

    def create_user(self, claims):

        user = super().create_user(claims)

        user.first_name = claims.get("given_name", "")
        user.last_name = claims.get("family_name", "")
        user.save()

        return user

    def update_user(self, user, claims):

        user.first_name = claims.get("given_name", "")
        user.last_name = claims.get("family_name", "")
        user.save()

        return user
