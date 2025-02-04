"""
今有丁一千五百萬，出兵四十萬。問：幾丁科一兵？
答曰： a 丁 b分 。
"""

#----- content starts here -----
"""
Suppose there are 15,000,000 adult males (丁), and 400,000 soldiers are to be drafted.
Question: how many males are required to provide one soldier?

Answer: *a* males and *b* fractional parts.
"""

# Total males
total_males = 15000000

# Soldiers to be drafted
soldiers = 400000

# Calculate how many males are required per soldier
丁_per_兵 = Fraction(total_males, soldiers)

# Extract the integer part and fractional part
a = 丁_per_兵.numerator // 丁_per_兵.denominator  # Integer part
b = 丁_per_兵 - a  # Fractional part

# Simplify the fractional part
b = Fraction(b.numerator, b.denominator)#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 5, Actual: 1/2"""
