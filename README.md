Roadwatch Data Processor
=========================

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.com/daniel-sasu/roadwatch-data-processor.svg?branch=master)](https://travis-ci.com/daniel-sasu/roadwatch-data-processor)

This is a small library build specifically for Project Roadwatch. This package is used to process, format and clean up the csv data on road accidents in France in order
to be integrated in a SQL database.   


> **Note:** The scripts are adapted for csv files published between 2005-2017.


Generate documentation
-----------------------
```
$ make doc
```

> **Note:** The documentation is generated using [sphinx](http://www.sphinx-doc.org/en/master/).

Run tests
------------
```
$ make test
```

Usage
------
Processing `caracteristiques-2017.csv` file.

```python
In [1]: from rw_data_proc import caracteristics

In [2]: df = caracteristics.process(path='files/caracteristiques-2017.csv')

In [3]: df.head()
Out[3]:
              lum  agg  int  atm  col                 adr   comm  dep gps       lat     long                date
num_acc
201700000001    5    2    1    1    1       rue nationale  59477  590   M  50.51326  2.92191 2017-01-11 18:20:00
201700000002    1    2    3    1    3    5 rue sonneville  59005  590   M  50.53611  2.95314 2017-02-13 16:30:00
201700000003    1    2    9    1    5    rue Jules Guesde  59052  590   M  50.52174  2.88786 2017-03-07 11:50:00
201700000004    1    2    1    1    6   46 rue Sonneville  59005  590   M  50.53723  2.95700 2017-04-22 13:00:00
201700000005    1    2    1    1    2  Rue roger salengro  59011  590   M  50.52999  2.93798 2017-05-20 12:30:00

```

About
------

This module is a part of a bigger project called 'Project Roadwatch'. Which is was in individual assignment as a part in the first year graduate program in Computer Science at Lille University, Faculty of Science and Technology.

**Supervising Professor:** Mickael Salson

**Author:** Daniel SASU

References
-----------
* [Base de données accidents corporels de la circulation](https://www.data.gouv.fr/fr/datasets/base-de-donnees-accidents-corporels-de-la-circulation/).
