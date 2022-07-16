from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


VERSION = '0.0.1'
DESCRIPTION = 'Hastebin API Wrapper'


setup(
    name='Hastebin',
    author='xrevix',
    description=DESCRIPTION,
    version=VERSION,
    url="https://github.com/xrevix/Hastebin",
    author_email='<xrevix666@gmail.com>',
    license='MIT License',
    keywords=['module', 'Hastebin', 'library', 'package', 'python'],
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    install_requires=['requests'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)