from setuptools import setup, find_packages

REQUIRED_PACKAGES = ['matplotlib', 'numpy', 'six']

print(find_packages())
setup(name='hartigan_diptest',
      version='1.0',
      description='Hartigan Diptest',
      author='nomel',
      author_email='nomel@nomel.org',
      url='https://github.com/nomel/hartigan_diptest',
      license='MIT',
      packages=find_packages(),
      package_data={'': ['qDiptab.pkl']},
      install_requires=REQUIRED_PACKAGES,
      classifiers=[
          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6'
      ]
)
