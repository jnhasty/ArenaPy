# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='ArenaPy',
    version='0.1.0',
    description='A simple python interface to the Are.na api',
    long_description=open('README.txt').read(),
    author='jnhasty',
    author_email='jnhasty@gmail.com',
    url='https://github.com/jnhasty/arenapy',
    packages=['arenapy'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
    keywords='arena rest api client',
    license='MIT',
    install_requires=[
        'requests',
    ],
    zip_safe=False
)
