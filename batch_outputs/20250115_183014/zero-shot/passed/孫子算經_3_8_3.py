"""
今有綿，九萬一千一百三十五觔，給與三萬六千四百五十四戶。問：戶得幾何？
術曰：置九萬一千一百三十五觔，為實；以三萬六千四百五十四戶，為法。除之，得二觔，不盡一萬八千二百二十七觔，以一十六乘之，得二十九萬一千六百三十二兩，以戶除之，即得。
答曰： a觔 。
"""

"""
To solve this problem, we need to calculate how much cotton (綿) each household (戶) receives. The total amount of cotton is 91,135 觔, and it is distributed among 36,454 households. The result will be in 觔 (jin) and possibly smaller units (兩, where 1 觔 = 16 兩).

Here is the Python code to compute the solution:



The variable `a` will contain the result in 觔 as a fraction. If you want to express the remainder in smaller units (兩), you can further calculate it as follows:


"""


from fractions import Fraction

# Total cotton in 觔
total_cotton = 91135

# Total households
total_households = 36454

# Cotton per household in 觔
a = Fraction(total_cotton, total_households)

# Result
a  # This will give the amount of cotton each household receives in 觔 (as a fraction).

# Whole 觔 each household receives
whole_jin = a.numerator // a.denominator

# Remaining fraction in 觔
remaining_jin = a - whole_jin

# Convert remaining 觔 to 兩 (1 觔 = 16 兩)
remaining_liang = remaining_jin * 16

# Result in 觔 and 兩
whole_jin, remaining_liang


"""


This will give the result in terms of whole 觔 and the remainder in 兩.
"""


"""
"""
