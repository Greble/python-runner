import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()


setup(
    name="greble-runner",
    version="0.0.1",
    packages=find_packages(),
    description="Greble python runner",
    long_description=README,
    author="Greble",
    author_email="info@greble.io",
    url="",
    install_requires=[
        "greble-flow>=0.0.1"
    ],
)
