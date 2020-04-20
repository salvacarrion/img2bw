from os import path
from setuptools import setup, find_packages

# Add long description
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Add requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Setup project
setup(name='img2bw',
      version='0.1.2',
      description='Command-line application to binarize images',
    long_description=long_description,
    long_description_content_type='text/markdown',
      url='https://github.com/salvacarrion/img2bw',
      author='Salva Carrión',
      license='MIT',
      packages=find_packages(),
      package_data={
          'data.raw': ['*.*'],
      },
      install_requires=requirements,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'img2bw = img2bw:main'
          ]
      },
      #test_suite='tests.coverage',
      )
