from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license_ = f.read()

setup(name='mbnames',
      version='0.1.0',
      description=
      'Utility functions for working with MusicBrainz or Last.fm artist credit and title strings.',
      long_description=readme,
      author='arcctgx',
      author_email='arcctgx@o2.pl',
      url='https://github.com/arcctgx/mbnames',
      license=license_,
      packages=find_packages(exclude='tests'))
