try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {"description": "A bunch of small tools that I made using Python.",
          "author": "Ulysses Carlos",
          "url": "N/A",
          "download_url": "Where to download it.",
          "author_email": "ucarlos1@student.gsu.edu",
          "version": "0.1",
          "install_requires": ['nose', 'mutagen'],
          "packages": ['Minor'],
          "scripts": [],
          "name": "uly-minor-programs-0.1"}


setup(**config)
