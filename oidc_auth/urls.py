""" Django url definitions. """

__author__ = "William Tucker"
__date__ = "2020-11-26"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from django.urls import include, path
from mozilla_django_oidc.urls import OIDCAuthenticateClass

from . import views


urlpatterns = [
    path("login/", OIDCAuthenticateClass.as_view(), name="login"),
    path("logout/", views.OIDCLogoutView.as_view(), name="logout"),
    path("oidc/", include("mozilla_django_oidc.urls")),
]
