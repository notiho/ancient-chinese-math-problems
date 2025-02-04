"""
今有錦一匹，直錢一萬八千。問：丈、尺、寸各直幾何？
術曰：置錢一萬八千，以四除之，得一丈之直；一退再退，得尺寸之直。
答曰：丈 a錢 ，尺 b錢 ，寸 c錢 。
"""

"""
To solve this problem, we will calculate the value of a single "丈" (zhang), "尺" (chi), and "寸" (cun) based on the given total value of the fabric (18,000 錢). The problem states that the value of one "丈" is obtained by dividing the total by 4, and the values of "尺" and "寸" are obtained by further dividing by 10 and 10 again, respectively.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total value of the fabric in 錢
total_value = 18000

# Calculate the value of one 丈 (zhang)
a = Fraction(total_value, 4)

# Calculate the value of one 尺 (chi)
b = Fraction(a, 10)

# Calculate the value of one 寸 (cun)
c = Fraction(b, 10)

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
