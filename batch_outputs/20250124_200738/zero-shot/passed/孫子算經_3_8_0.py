"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

"""
To solve this problem, we need to divide the total weight of cotton (91,135 觔) by the number of households (36,454 戶) to determine how much cotton each household receives. The remainder is then converted into smaller units (兩) and distributed among the households.

Here is the Python code to compute the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Total weight of cotton in 觔
total_cotton = 91135  # 觔

# Number of households
households = 36454  # 戶

# Divide total cotton by households to get the amount per household in 觔
a = total_cotton // households  # Quotient in 觔
remainder_cotton = total_cotton % households  # Remainder in 觔

# Convert the remainder into smaller units (1 觔 = 16 兩)
remainder_in_liang = remainder_cotton * 16  # Convert to 兩

# Distribute the remainder in 兩 among households
liang_per_household = Fraction(remainder_in_liang, households)  # Fractional amount in 兩

# Final result: each household gets `a` 觔 and `liang_per_household` 兩
a = Fraction(a) + liang_per_household / 16  # Convert 兩 back to 觔

# The answer is stored in variable `a`
a
#----- content ends here -----


"""


The variable `a` will contain the amount of cotton each household receives in 觔 (including fractional parts).
"""


"""
"""
