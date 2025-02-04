"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose a door is opened, leaving a gap of 1 chi from the lintel, and it does not close by 2 cun.
Question: what is the width of the door?

The procedure says: Take the gap of 1 chi from the lintel and square it. Divide the result by the 2 cun that it does not close, halved. Add half of the 2 cun that it does not close to the result, and this gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

from fractions import Fraction

# 去閫一尺 (gap from the lintel)
去閫 = 1  # in chi

# 不合二寸 (does not close by 2 cun)
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘 (square the gap)
平方 = 去閫 ** 2

# 以不合二寸半之而一 (divide the square by half of the "does not close" value)
半不合 = 不合 / 2
商 = 平方 / 半不合

# 增不合之半 (add half of the "does not close" value)
門廣 = 商 + 半不合

# Convert to zhang (1 zhang = 10 chi)
a = 門廣 / 10  # in zhang

a#----- content ends here -----

"""
"""
