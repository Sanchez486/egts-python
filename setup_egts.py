NAME = 'egts'
DESCRIPTION = 'Enocder interface for creating EGTS messages'
URL = 'https://github.com/Sanchez486/egts-python/'
EMAIL = 'fergusonalexandr@mail.ru'
AUTHOR = 'Sanchez486'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = '0.1.0'

from setuptools import setup

setup(name=NAME,
      version='0.1.0',
      description=DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,
      license='MIT',
      packages=['egts'],
      zip_safe=False)
