#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='signed-requests',
    version='0.0.1',
    description='Signed Authentication for Python Requests',
    author='Arnar Yngvason',
    author_email='arnar@greenqloud.com',
    url='https://github.com/demux/signed-requests',
    long_description=open('readme.md', 'r').read(),
    packages=[
        'signed_requests',
    ],
    requires=[
        'requests',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)