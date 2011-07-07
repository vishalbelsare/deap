#!/usr/bin/env python

from distutils.core import setup

import deap

setup(name='deap',
      version=deap.__version__,
      description='Distributed Evolutionary Algorithms in Python',
      long_description=open('README.txt').read(),
      author='deap Development Team',
      author_email='deap-users@googlegroups.com',
      url='http://deap.googlecode.com',
      download_url='http://code.google.com/p/deap/downloads/list',
      packages=['deap', 'deap.benchmarks', 'deap.dtm', 'deap.dtm.tests', 'deap.tests'],
      platforms=['any'],
      keywords=['evolutionary algorithms','genetic algorithms','genetic programming','cma-es','ga','gp','es'],
      license='LGPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        ],
     )