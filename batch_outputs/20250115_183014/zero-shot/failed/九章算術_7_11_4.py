"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall of 5 feet thickness. The larger mouse doubles its progress each day, while the smaller mouse halves its progress each day. We need to determine how many days it takes for them to meet and how far each mouse has dug.

Here is the Python code:


"""


from fractions import Fraction

# Given data
wall_thickness = 5  # in feet
large_mouse_rate = 1  # initial rate in feet/day
small_mouse_rate = 1  # initial rate in feet/day

# Using the "盈不足術" (excess and deficiency method)
# After 2 days, the total progress is less than the wall thickness by 5/10 feet (5 inches).
# After 3 days, the total progress exceeds the wall thickness by 3 + 7/10 feet (3 feet 7 inches).

# Deficiency after 2 days
deficiency = Fraction(5, 10)  # 5 inches = 5/10 feet

# Excess after 3 days
excess = Fraction(3, 1) + Fraction(7, 10)  # 3 feet 7 inches = 3 + 7/10 feet

# Rate of change (difference in days)
rate_of_change = 3 - 2  # 1 day

# Total rate of progress per day (large mouse + small mouse)
total_rate = (excess + deficiency) / rate_of_change

# Time to meet (wall thickness divided by total rate)
a = wall_thickness / total_rate

# Distance dug by each mouse
# Large mouse doubles its progress each day
# Small mouse halves its progress each day
b = large_mouse_rate * (2 ** (a - 1))  # Distance dug by the large mouse
c = small_mouse_rate * (1 / (2 ** (a - 1)))  # Distance dug by the small mouse

# Results
a = a  # Time in days
b = b  # Distance dug by the large mouse in feet
c = c  # Distance dug by the small mouse in feet


"""


### Explanation:
1. We use the "盈不足術" (excess and deficiency method) to calculate the total rate of progress per day.
2. The total rate is determined by the difference between the excess and deficiency over the change in days.
3. The time to meet (a) is calculated by dividing the wall thickness by the total rate.
4. The distances dug by the large mouse (b) and the small mouse (c) are calculated based on their respective progress rates.

### Final Values:
- `a`: Time in days for the mice to meet.
- `b`: Distance dug by the large mouse in feet.
- `c`: Distance dug by the small mouse in feet.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 25/21
Variable 'b' has wrong value. Expected: 59/17, Actual: 1.141140309994013
Variable 'c' has wrong value. Expected: 26/17, Actual: 0.8763164277364337"""
