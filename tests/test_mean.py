from codac import *

from pyintervalstats.data import IntervalData
from pyintervalstats.interval_statistics import interval_mean


data = IntervalData([
    [1, 2],
    [3, 4],
    [5, 6]
])

mean = interval_mean(data)

print("Interval mean:", mean)