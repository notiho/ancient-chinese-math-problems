"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
Here is the Python code that computes the values of the unknowns `a`, `b`, and `c`:


"""


from fractions import Fraction

# Given data
total_money = 18000  # in 錢

# Calculations
a = Fraction(total_money, 4)  # 一丈之直
b = Fraction(a, 10)          # 一尺之直 (1丈 = 10尺)
c = Fraction(b, 10)          # 一寸之直 (1尺 = 10寸)

# Results
a, b, c


"""


This code calculates the value of `a` (錢 per 丈), `b` (錢 per 尺), and `c` (錢 per 寸) using the given method.
"""


"""
"""
