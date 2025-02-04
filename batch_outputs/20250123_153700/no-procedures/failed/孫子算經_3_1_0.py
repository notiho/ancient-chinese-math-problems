"""
今有丁一千五百萬，出兵四十萬。問：幾丁科一兵？
答曰： a 丁 b分 。
"""

"""
Suppose there are 15,000,000 adult males (丁), and 400,000 soldiers are to be conscripted.
Question: how many adult males are required to provide one soldier?

Answer: *a* adult males and *b* fractional parts.
"""

# Total adult males
total_adult_males = 15000000

# Total soldiers
total_soldiers = 400000

# Calculate the number of adult males required per soldier
丁_per_兵 = Fraction(total_adult_males, total_soldiers)

# Extract the integer part and fractional part
a = 丁_per_兵.numerator // 丁_per_兵.denominator  # Integer part
b = 丁_per_兵 - a  # Fractional part

# Final result
a = a
b = 丁_per_兵 - Fraction(a)
"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
