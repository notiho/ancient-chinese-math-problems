"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
To solve the problem using Python, we will translate the ancient Chinese math problem into code. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given equations:
# 2a + b = 96
# 2a + 3b = 144

# Subtract the first equation from the second:
# (2a + 3b) - (2a + b) = 144 - 96
# 2b = 48
b = Fraction(48, 2)  # Solve for b
b = 24  # b represents the money held by person 乙

# Substitute b back into the first equation:
# 2a + b = 96
# 2a + 24 = 96
# 2a = 96 - 24
# 2a = 72
a = Fraction(72, 2)  # Solve for a
a = 36  # a represents the money held by person 甲

# Final answer:
# a = 36 (money held by 甲)
# b = 24 (money held by 乙)
#----- content ends here -----


"""


Now, the variables `a` and `b` hold the respective amounts of money for 甲 and 乙.
"""


"""
"""
