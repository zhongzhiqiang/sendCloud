from setuptools import setup

PACKAGE = "sendCloud"
NAME = "sendCloud"
DESCRIPTION = "send cloud web api"
AUTHOR = "zhongzq"
VERSION = '0.2'

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license="BSD",
    packages=[PACKAGE],
    install_requires=[
        'requests==2.12.4',
        'voluptuous==0.9.3',
    ],
    zip_safe=False,
)
