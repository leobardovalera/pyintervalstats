"""
data.py

Core data structures for PyIntervalStats.
"""

from codac import Interval, IntervalVector


class IntervalData:
    """
    Represents a dataset of interval observations.

    Supported input formats (Version 0.1):
        - IntervalVector
        - list of Interval
        - list of [lower, upper]
    """

    def __init__(self, data):

        if isinstance(data, IntervalVector):
            self._data = data

        elif isinstance(data, list):

            if len(data) == 0:
                self._data = IntervalVector(0)

            elif all(isinstance(x, Interval) for x in data):
                self._data = IntervalVector(data)

            elif all(
                isinstance(x, (list, tuple))
                and len(x) == 2
                for x in data
            ):
                intervals = [Interval(a, b) for a, b in data]
                self._data = IntervalVector(intervals)

            else:
                raise TypeError("Unsupported list format.")

        else:
            raise TypeError(
                f"Unsupported input type: {type(data)}"
            )

    @property
    def data(self):
        """Return the underlying CODAC IntervalVector."""
        return self._data

    def size(self):
        """Return the number of intervals."""
        return self._data.size()

    def __len__(self):
        return self.size()

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        return f"IntervalData({self._data})"