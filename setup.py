import re
from codecs import open
from os import path, environ
from setuptools import setup

PACKAGE_NAME = 'variable-engine'

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

    
class Version:
    def __init__(self, major: int = 0, minor: int = 0, micro: int = 0):
        self.major = major
        self.minor = minor
        self.micro = micro
    
__version__ = Version(major = 0, minor = 1, micro = 3)
VERSION = f'{__version__.major}.{__version__.minor}.{__version__.micro}'

setup(
    name = PACKAGE_NAME,
    version = VERSION,
    author = 'Ngtfury',
    author_email = 'furyff143@gmail.com',
    description = 'A simple package for handling variables in string.',
    include_package_data = True,
    license = "MIT License",
    long_description = README,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Ngtfury/variable-engine',
    packages = ['variable_engine'],
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    
)
