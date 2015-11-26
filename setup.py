#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="Flask Docker Deploy",
    version="0.1",
    description="Show deployment of a Flask application with Docker",
    packages=find_packages(),
    install_requires=[
        "flask>=0.10",
)
