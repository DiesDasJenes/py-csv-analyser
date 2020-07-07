========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|  |requires|
        | |coveralls| |codecov|
    * - package
      - | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/py-csv-analyser/badge/?version=latest
    :target: https://readthedocs.org/projects/py-csv-analyser
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/DiesDasJenes/py-csv-analyser.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/DiesDasJenes/py-csv-analyser

.. |requires| image:: https://requires.io/github/DiesDasJenes/py-csv-analyser/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/diesdasjenes/py-csv-analyser/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/github/DiesDasJenes/py-csv-analyser/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/r/diesdasjenes/py-csv-analyser

.. |codecov| image:: https://codecov.io/gh/diesdasjenes/py-csv-analyser/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/diesdasjenes/py-csv-analyser

.. |commits-since| image:: https://img.shields.io/github/commits-since/diesdasjenes/py-csv-analyser/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/diesdasjenes/py-csv-analyser/compare/v0.0.0...master

.. end-badges

This will help analyse csv files which has to be done in excel. I hope to ease the analysis for certain people.

* Free software: MIT license

Installation
============

::

    pip install py-csv-analyser

You can also install the in-development version with::

    pip install https://github.com/diesdasjenes/py-csv-analyser/archive/master.zip


Documentation
=============


https://py-csv-analyser.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
