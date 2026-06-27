from pyintervalstats.data import IntervalData
from pyintervalstats.interval_statistics import interval_quartiles

data = IntervalData([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

q1, q2, q3 = interval_quartiles(data)

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)