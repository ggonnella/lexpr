#
# (c) 2023 Giorgio Gonnella, University of Goettingen, Germany
#
from setuptools import setup, find_packages

def readme():
  with open('README.md') as f:
    return f.read()

import sys
if not sys.version_info[0] == 3:
  sys.exit("Sorry, only Python 3 is supported")

setup(name='lexpr',
      version='0.1',
      description=\
        'A parser for simple logical expressions of identifiers',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='https://github.com/ggonnella/lexpr',
      keywords="bioinformatics sequence features",
      author='Giorgio Gonnella',
      author_email='gonnella@zbh.uni-hamburg.de',
      license='ISC',
      # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
      ],
      packages=find_packages(),
      install_requires=['lark'],
      zip_safe=False,
      include_package_data=True,
      package_data={"": ["data/lepr.g"]},
    )
