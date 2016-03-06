#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-git',
    version='0.1.0',
    description='Get git information for your django repository',

    author='Serafeim Papastefanos',
    author_email='spapas@gmail.com',
    license='MIT',
    url='https://github.com/spapas/django-git/',
    zip_safe=False,
    include_package_data=False,
    packages=find_packages(exclude=['tests.*', 'tests', 'sample', ]),

    install_requires=['Django >=1.4', 'six', 'GitPython > 1.0'],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
)
