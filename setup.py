from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='img2bw',
      version='0.1',
      description='Image binarizer',
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
