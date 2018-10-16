import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-brazilian-addresses',
    version='0.1',
    packages=[
        'addresses',
        'addresses.management',
        'addresses.management.commands',
        'addresses.templates',
        'addresses.templates.addresses',
        'addresses.migrations',
    ],
    include_package_data=True,
    license='License MIT',
    description='A django client library for Brazilian Correios API\'s, current solution available to find addresses by zipcode, calculate the shipping service and tracking.',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Felipe Frizzo',
    author_email='felipefrizzo@gmail.com',
    url='felipefrizzo.github.io',
    python_requires="!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=1.9',
        'djangorestframework>=3.8.2',
        'requests>=2.19.1'
    ],
)
