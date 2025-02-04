"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
答曰： a日 。
"""

#----- content starts here -----
"""
Suppose there are three daughters:
- The eldest daughter returns home every 5 days.
- The middle daughter returns home every 4 days.
- The youngest daughter returns home every 3 days.

Question: After how many days will all three daughters return home on the same day?

Answer: *a* days.
"""

# Define the return intervals for the three daughters
eldest = 5
middle = 4
youngest = 3

# Find the least common multiple (LCM) of the three intervals
# The LCM is the smallest number divisible by all three intervals
a = eldest
while a % middle != 0 or a % youngest != 0:
    a += eldest

# The result is stored in `a` as the number of days when all three daughters will meet.#----- content ends here -----

"""
"""
