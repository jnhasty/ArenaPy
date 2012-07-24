from setuptools import setup

setup(
    name='arenapy',
    version='0.1',
    description='A simple python interface to the Are.na api',
    author='jnhasty',
    author_email='jnhasty@gmail.com',
    url='http://are.na',
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
        'setuptools',
        'requests',
    ],
)
