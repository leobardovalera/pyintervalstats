# PyIntervalStats Architecture

## Purpose

PyIntervalStats is an open-source Python library for computing statistics under interval and fuzzy uncertainty.

The project implements the algorithms described in

> Nguyen, Hung T., Vladik Kreinovich, Berlin Wu, and Gang Xiang. *Computing Statistics under Interval and Fuzzy Uncertainty*. Vol. 130. Springer Verlag, Berlin, Heidelberg, 2012.

using the CODAC library as the primary backend for interval computations.

---

# Design Philosophy

PyIntervalStats is designed as a scientific software library rather than a collection of independent scripts.

The main objectives are:

* Simplicity
* Readability
* Extensibility
* Reproducibility
* Scientific correctness

Every component should have a single responsibility and be easy to test independently.

---

# Design Principles

## Dataset-Oriented

The library is intended to analyze complete interval datasets instead of isolated interval numbers.

All statistical algorithms operate on datasets.

---

## Multiple Input Formats

The library should support multiple input formats, including

* CSV files
* Excel files
* JSON files
* Python lists
* NumPy arrays
* Pandas DataFrames
* CODAC interval objects

Users should not need to modify the statistical algorithms depending on the input format.

---

## Internal Representation

All supported input formats are converted into a common internal representation.

Future statistical algorithms will operate only on this internal representation.

---

## Separation of Responsibilities

The software architecture separates

* Data input
* Data representation
* Statistical algorithms
* Output generation

Each module should perform one well-defined task.

---

## Computational Backend

PyIntervalStats uses CODAC for

* interval arithmetic
* interval vectors
* interval constraint programming
* contractors
* separators

Statistical algorithms are implemented independently of the computational backend whenever possible.

---

## User Interface

The library should expose a simple and intuitive interface.

Example:

```python
from pyintervalstats import IntervalDataset
from pyintervalstats import interval_mean

data = IntervalDataset("measurements.csv")

mean = interval_mean(data)
```

The same interface should work regardless of the original data source.

---

## Extensibility

New statistical algorithms should be added without modifying existing implementations.

The architecture should facilitate future extensions while maintaining backward compatibility.

---

# Initial Algorithms

The first implementation stage will include

1. Mean
2. Median
3. Quantiles
4. Variance
5. Covariance
6. Correlation

Additional algorithms from the reference book will be incorporated progressively.

---

# Long-Term Vision

The objective of PyIntervalStats is to become a modern, open-source reference implementation of interval statistical algorithms for research, education, and practical applications.

