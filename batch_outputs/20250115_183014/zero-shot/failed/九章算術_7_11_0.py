"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves two mice digging through a wall of thickness 5 feet. Each mouse digs at a rate of 1 foot per day, but the larger mouse doubles its progress daily, while the smaller mouse halves its progress daily. We are tasked with finding the number of days until they meet and the distance each mouse has dug.

Here is the Python code:


"""


from fractions import Fraction

# Wall thickness
wall_thickness = 5  # in feet

# Rates of progress
large_mouse_rate = 1  # in feet per day
small_mouse_rate = 1  # in feet per day

# Large mouse doubles its progress daily
# Small mouse halves its progress daily

# Using the "盈不足術" (excess and deficiency method):
# After 2 days, the total progress is less than the wall thickness by 5 inches (5/12 feet).
# After 3 days, the total progress exceeds the wall thickness by 3 feet 7.5 inches (3 + 7.5/12 feet).

# Convert the given data into fractions
less_deficiency = Fraction(5, 12)  # 5 inches = 5/12 feet
excess = Fraction(3) + Fraction(7.5, 12)  # 3 feet 7.5 inches = 3 + 7.5/12 feet

# Calculate the difference in days and rates
days_difference = 3 - 2  # 3 days - 2 days = 1 day
rate_difference = excess + less_deficiency  # excess + deficiency

# Calculate the rate of progress per day
rate_per_day = rate_difference / days_difference

# Calculate the total number of days until they meet
a = wall_thickness / rate_per_day

# Calculate the distance each mouse digs
b = large_mouse_rate * (2 ** (a - 1))  # Large mouse's total distance
c = small_mouse_rate * (1 / (2 ** (a - 1)))  # Small mouse's total distance

# Results
a = float(a)  # Convert to float for clarity
b = float(b)
c = float(c)

# The results are:
# a: Number of days until they meet
# b: Distance dug by the large mouse
# c: Distance dug by the small mouse


"""


This code calculates the number of days (`a`) until the two mice meet, as well as the distances dug by the large mouse (`b`) and the small mouse (`c`). The calculations use the "盈不足術" (excess and deficiency method) as described in the problem.
"""


"""
Code error: both arguments should be Rational instances"""
