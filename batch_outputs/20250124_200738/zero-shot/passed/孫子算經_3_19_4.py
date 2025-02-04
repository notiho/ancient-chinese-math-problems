"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
Here is the Python code to solve the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 18000  # in 錢

# Calculations
a = Fraction(total_money, 4)  # Price of one 丈
b = Fraction(a, 10)          # Price of one 尺 (1 丈 = 10 尺)
c = Fraction(b, 10)          # Price of one 寸 (1 尺 = 10 寸)

# Results
a, b, c
#----- content ends here -----


"""


This will compute the values of `a`, `b`, and `c` as fractions. The results are:

- `a` (丈) = 4500 錢
- `b` (尺) = 450 錢
- `c` (寸) = 45 錢
"""


"""
"""
