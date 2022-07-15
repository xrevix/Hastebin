from setuptools import setup

VERSION = '0.1'
DESCRIPTION = 'Hastebin API Wrapper'


setup(
    name='Hastebin',
    version='0.1',
    license='MIT License',
    description='Hastebin API Wrapper',
    author='xrevix',
    url="https://github.com/xrevix/Hastebin",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    author_email='<xrevix666@gmail.com>',
    keywords=['module', 'Hastebin', 'library', 'package', 'python'],
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
  install_requires = ['requests']
)
