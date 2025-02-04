"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a(=101/100)丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is 1 chi away from the lintel and does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the lintel, 1 chi, and square it. 
From the result, subtract half of the amount it does not close by, 2 cun, and divide by 1. 
Add half of the amount it does not close by to the result, and this gives the width of the door.

Answer: *a*(=101/100) zhang.
"""

from fractions import Fraction

# 去閫一尺
去閫 = 1  # chi

# 不合二寸
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘，所得
去閫平方 = 去閫 ** 2

# 以不合二寸半之而一，所得
半不合 = 不合 / 2
所得 = (去閫平方 - 半不合) / 1

# 增不合之半，即得門廣
門廣 = 所得 + 半不合

a = 門廣  # 101/100 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 1"""
