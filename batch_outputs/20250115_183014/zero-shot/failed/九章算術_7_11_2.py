"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall, with their progress rates doubling and halving respectively. We need to compute the number of days until they meet and the distances each mouse has dug.

Here is the Python code:


"""


from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in 尺

# Rates of digging
big_mouse_rate = 1  # in 尺 per day
small_mouse_rate = 1  # in 尺 per day

# Progress doubling and halving
big_mouse_progress = big_mouse_rate * 2  # in 尺 per day
small_mouse_progress = small_mouse_rate / 2  # in 尺 per day

# Using the 盈不足 (excess and deficiency) method
# After 2 days, the deficiency is 5寸 = 5/10尺 = 1/2尺
# After 3 days, the excess is 3尺7寸半 = 3 + 7/10 + 5/100 = 3 + 75/100 = 3 + 3/4 = 15/4尺

# Deficiency and excess
deficiency = Fraction(1, 2)  # in 尺
excess = Fraction(15, 4)  # in 尺

# Days corresponding to deficiency and excess
days_deficiency = 2  # days
days_excess = 3  # days

# 盈不足術 (excess and deficiency method)
rate_difference = days_excess - days_deficiency  # in days
total_difference = excess + deficiency  # in 尺

# Compute the number of days until they meet
a = total_difference / rate_difference  # in days

# Compute the distances each mouse digs
b = big_mouse_progress * a  # distance dug by the big mouse in 尺
c = small_mouse_progress * a  # distance dug by the small mouse in 尺

# Results
a = float(a)
b = float(b)
c = float(c)

# Output the results
a, b, c


"""


Explanation of the solution:
1. The wall thickness is given as 5 尺.
2. The big mouse and small mouse dig at rates of 1 尺 per day, but their progress doubles and halves respectively.
3. After 2 days, the deficiency is 5 寸 (converted to 尺 as 1/2 尺).
4. After 3 days, the excess is 3 尺 7 寸 5 分 (converted to 尺 as 15/4 尺).
5. Using the 盈不足 (excess and deficiency) method, we calculate the number of days until they meet (`a`), and the distances each mouse digs (`b` and `c`).

The variables `a`, `b`, and `c` represent the number of days until they meet, the distance dug by the big mouse, and the distance dug by the small mouse, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 4.25
Variable 'b' has wrong value. Expected: 59/17, Actual: 8.5
Variable 'c' has wrong value. Expected: 26/17, Actual: 2.125"""
