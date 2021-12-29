import re
from codecs import open
from os import path, environ
from setuptools import setup

PACKAGE_NAME = 'variable-engine'
VERSION = '0.1.0'

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

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