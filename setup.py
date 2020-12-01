""" Setup module for installation. """

__author__ = "William Tucker"
__date__ = "2020-09-21"
__copyright__ = "Copyright 2020 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"


from setuptools import setup, find_packages


with open("README.md") as readme_file:
    long_description = readme_file.read()


setup(
    name="django-oidc-extras",
    version="0.1",
    description="Extra utilities for Django apps using mozilla-django-oidc.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/cedadev/django-oidc-backend",
    author="William Tucker",
    author_email="william.tucker@stfc.ac.uk",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "mozilla-django-oidc",
    ],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
