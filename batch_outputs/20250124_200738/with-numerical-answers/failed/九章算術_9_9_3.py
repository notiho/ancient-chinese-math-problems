"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a(=101/100)丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is one chi away from the threshold and does not close by two cun.
Question: how wide is the door?

The procedure says: Square the distance from the threshold (1 chi), obtaining a result.
Divide this result by the amount it does not close (2 cun), halving it to obtain another result.
Add half of the amount it does not close to this result, and the width of the door is obtained.

The answer says: *a*(=101/100) zhang.
"""

from fractions import Fraction

# 去閫一尺
去閫 = 1  # chi

# 不合二寸
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘，所得
平方 = 去閫 * 去閫

# 以不合二寸半之而一，所得
半之 = 平方 / 不合

# 增不合之半，即得門廣
門廣 = 半之 + (不合 / 2)

a = Fraction(門廣)  # 101/100 zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 51/10"""
