"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is 1 chi away from the threshold and does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the threshold (1 chi) and square it. 
Divide the result by the amount it does not close (2 cun), halved, and then add half of the amount it does not close.
This gives the width of the door.

Answer: *a* zhang.
"""

from fractions import Fraction

# 去閫一尺 (distance from the threshold)
去閫 = 1  # in chi

# 不合二寸 (does not close by 2 cun)
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘 (square the distance from the threshold)
去閫平方 = 去閫 ** 2

# 以不合二寸半之而一 (divide the squared distance by half of the amount it does not close)
半不合 = 不合 / 2
商 = 去閫平方 / 半不合

# 增不合之半 (add half of the amount it does not close)
門廣 = 商 + 半不合

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)

a  # The width of the door in zhang#----- content ends here -----

"""
"""
