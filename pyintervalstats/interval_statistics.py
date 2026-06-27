"""
interval_statistics.py

Statistical algorithms for interval-valued data.
"""

from codac import Interval
from .data import IntervalData


def interval_mean(data):
    """
    Compute the interval arithmetic mean.

    Parameters
    ----------
    data : IntervalData

    Returns
    -------
    Interval
        Interval containing all possible arithmetic means.
    """

    if not isinstance(data, IntervalData):
        raise TypeError("data must be an IntervalData object.")

    if len(data) == 0:
        raise ValueError("The dataset is empty.")

    lower_sum = 0.0
    upper_sum = 0.0

    for interval in data:
        lower_sum += interval.lb()
        upper_sum += interval.ub()

    n = len(data)

    return Interval(lower_sum / n, upper_sum / n)

def interval_median(data):
    """
    Compute the interval median.
    """

    if not isinstance(data, IntervalData):
        raise TypeError("data must be an IntervalData object.")

    if len(data) == 0:
        raise ValueError("The dataset is empty.")

    lower = sorted(interval.lb() for interval in data)
    upper = sorted(interval.ub() for interval in data)

    n = len(data)

    if n % 2 == 1:
        lower_median = lower[n // 2]
        upper_median = upper[n // 2]
    else:
        lower_median = (lower[n // 2 - 1] + lower[n // 2]) / 2.0
        upper_median = (upper[n // 2 - 1] + upper[n // 2]) / 2.0

    return Interval(lower_median, upper_median)