"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is 1 chi away from the lintel (閫), and it does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the lintel (1 chi) and square it. 
Divide the result by the amount it does not close (2 cun), halved and taken as 1.
Add half of the amount it does not close to the result, and this gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

from fractions import Fraction

# 去閫一尺 (1 chi = 1/10 zhang)
去閫 = Fraction(1, 10)  # Convert chi to zhang

# 不合二寸 (1 cun = 1/100 zhang)
不合 = Fraction(2, 100)  # Convert cun to zhang

# 以去閫一尺自乘，所得
平方 = 去閫 ** 2

# 以不合二寸半之而一，所得
半不合 = 不合 / 2
商 = 平方 / 半不合

# 增不合之半，即得門廣
門廣 = 商 + 半不合

a = 門廣
a#----- content ends here -----

"""
"""
