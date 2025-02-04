"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall, with their progress rates changing daily. We need to calculate the number of days until they meet and the distance each mouse has dug.

Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in 尺

# Rates of progress
big_mouse_rate_day1 = 1  # in 尺 per day
small_mouse_rate_day1 = 1  # in 尺 per day

# Progress multipliers
big_mouse_multiplier = 2  # Big mouse doubles its progress each day
small_mouse_multiplier = Fraction(1, 2)  # Small mouse halves its progress each day

# Initialize variables
big_mouse_total = 0  # Total distance dug by the big mouse
small_mouse_total = 0  # Total distance dug by the small mouse
days = 0  # Number of days

# Simulate the digging process
while big_mouse_total + small_mouse_total < wall_thickness:
    days += 1
    big_mouse_progress = big_mouse_rate_day1 * (big_mouse_multiplier ** (days - 1))
    small_mouse_progress = small_mouse_rate_day1 * (small_mouse_multiplier ** (days - 1))
    big_mouse_total += big_mouse_progress
    small_mouse_total += small_mouse_progress

# Assign results to variables
a = days
b = big_mouse_total
c = small_mouse_total

# Results
a, b, c
#----- content ends here -----


"""


### Explanation:
1. The wall thickness is 5 尺.
2. The big mouse starts digging at a rate of 1 尺 per day and doubles its progress each day.
3. The small mouse starts digging at a rate of 1 尺 per day and halves its progress each day.
4. We simulate the digging process day by day, summing up the distances dug by both mice until their combined progress equals or exceeds the wall thickness.
5. The number of days (`a`), the distance dug by the big mouse (`b`), and the distance dug by the small mouse (`c`) are calculated and stored in variables.

### Output:
The variables `a`, `b`, and `c` will contain the number of days, the distance dug by the big mouse, and the distance dug by the small mouse, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 3
Variable 'b' has wrong value. Expected: 59/17, Actual: 7
Variable 'c' has wrong value. Expected: 26/17, Actual: 7/4"""
