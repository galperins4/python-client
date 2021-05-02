import sys

import setuptools


requires = [
    'requests>=2.19.1',
    'backoff>=1.6.0',
    'flatten_dict>=0.3.0'
]

tests_require = []

extras_require = {}

setuptools.setup(
    name='hedora-python-client',
    description='Python API client for Hedora Hashgraph.',
    version='0.0.1',
    author='TBD',
    author_email='TBD',
    url='https://github.com/galperins4/hedora-python-client',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    install_requires=requires,
    extras_require=extras_require,
    tests_require=tests_require,
)
