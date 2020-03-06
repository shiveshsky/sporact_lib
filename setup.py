import setuptools

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setuptools.setup(
    name="sporact_lib",
    version="0.1.0",
    packages=find_packages(),  # fix
    description="Sporact base actions for mistral",
)
