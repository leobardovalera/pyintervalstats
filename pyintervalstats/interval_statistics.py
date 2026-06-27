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

def percentile(values, p):
    """
    Compute the p-th percentile of a list of real numbers.

    Parameters
    ----------
    values : list
        List of real numbers.
    p : float
        Percentile between 0 and 1.

    Returns
    -------
    float
    """

    if not (0.0 <= p <= 1.0):
        raise ValueError("p must be between 0 and 1.")

    values = sorted(values)
    n = len(values)

    if n == 0:
        raise ValueError("The list is empty.")

    position = p * (n - 1)

    lower_index = int(position)
    upper_index = lower_index + 1

    if upper_index >= n:
        return values[-1]

    fraction = position - lower_index

    return values[lower_index] + fraction * (
        values[upper_index] - values[lower_index]
    )


def interval_quartiles(data):
    """
    Compute the interval quartiles Q1, Q2, and Q3.

    Parameters
    ----------
    data : IntervalData

    Returns
    -------
    tuple
        (Q1, Q2, Q3)
    """

    if not isinstance(data, IntervalData):
        raise TypeError("data must be an IntervalData object.")

    if len(data) == 0:
        raise ValueError("The dataset is empty.")

    lower = sorted(interval.lb() for interval in data)
    upper = sorted(interval.ub() for interval in data)

    q1 = Interval(
        percentile(lower, 0.25),
        percentile(upper, 0.25)
    )

    q2 = interval_median(data)

    q3 = Interval(
        percentile(lower, 0.75),
        percentile(upper, 0.75)
    )

    return q1, q2, q3