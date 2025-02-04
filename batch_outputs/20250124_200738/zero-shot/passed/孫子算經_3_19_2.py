"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
Here is the Python code to compute the values of the unknowns `a`, `b`, and `c`:


"""

#----- content starts here -----

from fractions import Fraction

# Total value of the silk in money
total_money = 18000

# Calculations
a = Fraction(total_money, 4)  # Value of one 丈
b = Fraction(a, 10)          # Value of one 尺 (1 丈 = 10 尺)
c = Fraction(b, 10)          # Value of one 寸 (1 尺 = 10 寸)

# Results
a, b, c
#----- content ends here -----


"""


This will compute:
- `a` as the value of one 丈 in 錢,
- `b` as the value of one 尺 in 錢,
- `c` as the value of one 寸 in 錢.
"""


"""
"""
