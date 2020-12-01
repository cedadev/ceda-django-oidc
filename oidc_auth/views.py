""" App views module. """

__author__ = "William Tucker"
__date__ = "2020-11-25"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from mozilla_django_oidc.views import OIDCLogoutView


class GetOIDCLogoutView(OIDCLogoutView):
    """ Extends the OIDC logout view to support GET method logout.
    Not recommended. """

    def get(self, request):
        return self.post(request)
