from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='inline-keyboard-paginator',
    version='0.0.1',
    packages=['inline_keyboard_paginator'],
    url='https://github.com/LordDeveLoper/inline-keyboard-paginator',
    license='GPL2',
    author='LordDeveloper',
    author_email='sadeghij87@gmail.com',
    description='Python inline keyboard pagination MTProto libraries',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='telegram bot api pagination keyboard inline tools',
)
