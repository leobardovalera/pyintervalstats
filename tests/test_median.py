from pyintervalstats.data import IntervalData
from pyintervalstats.interval_statistics import interval_median

data = IntervalData([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("Interval median:", interval_median(data))

data = IntervalData([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
])

print("Interval median:", interval_median(data))