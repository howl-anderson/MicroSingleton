from distutils.core import setup
from setuptools import find_packages

setup(
    name='micro_singleton',
    version='0.1.0',
    install_requires=[
        'psutil',
        'enum34'
    ],
    packages=find_packages(exclude=[]),
    license='GPL',
    author='Xiaoquan Kong',
    author_email='u1mail2me@gmail.com',
    description='library for MicroSingleton pattern (application and class level)'
)
