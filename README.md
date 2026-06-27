# PyIntervalStats

*A Python library for computing statistics under interval and fuzzy uncertainty.*

## Overview

PyIntervalStats is an open-source Python library that implements algorithms for computing statistical quantities under interval and fuzzy uncertainty.

The project is inspired by the algorithms presented in the book

> Nguyen, Hung T., Vladik Kreinovich, Berlin Wu, and Gang Xiang. *Computing Statistics under Interval and Fuzzy Uncertainty*. Vol. 130. Springer Verlag, Berlin, Heidelberg, 2012.

The objective of this project is to provide a modern, documented, and reusable implementation of these algorithms using Python.

## Motivation

Despite the importance of interval statistics in reliable computing, uncertainty quantification, engineering, and applied mathematics, there is currently no widely adopted open-source Python library implementing the algorithms described in the above reference.

PyIntervalStats aims to fill this gap by providing a free, well-documented, and extensible software package for researchers, educators, and practitioners.

## Dependencies

PyIntervalStats uses the CODAC library for interval arithmetic and interval constraint programming.

Reference:

> Rohou, Simon, Benoît Desrochers, and François Le Bars. *The Codac Library*. *Acta Cybernetica* 26, no. 4 (2024): 871–887. https://doi.org/10.14232/actacyb.302772

Additional optional backends may be incorporated in future versions.

## Current Status

This project is under active development.

The initial release will focus on implementing algorithms for:

* Interval mean
* Interval median and quantiles
* Interval variance
* Interval covariance
* Interval correlation

Additional algorithms described in the reference book will be incorporated progressively.

## Roadmap

* Initial project structure
* Core interval statistics
* Advanced statistical algorithms
* Documentation and examples
* Validation against published algorithms
* Community contributions

## Contributing

Contributions, suggestions, bug reports, and discussions are welcome.

## License

The license will be specified before the first public software release.

## Acknowledgments

The author gratefully acknowledges the contributions of the interval analysis and reliable computing community, particularly the authors of the reference book and the developers of CODAC, whose work inspired this project.

## References

1. Nguyen, Hung T., Vladik Kreinovich, Berlin Wu, and Gang Xiang. *Computing Statistics under Interval and Fuzzy Uncertainty*. Vol. 130. Springer Verlag, Berlin, Heidelberg, 2012.

2. Rohou, Simon, Benoît Desrochers, and François Le Bars. *The Codac Library*. *Acta Cybernetica* 26, no. 4 (2024): 871–887. https://doi.org/10.14232/actacyb.302772

