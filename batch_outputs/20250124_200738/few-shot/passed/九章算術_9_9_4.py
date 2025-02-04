"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is one chi away from the threshold and does not close by two cun.
Question: how wide is the door?

The procedure says: Take the distance from the threshold (1 chi) and square it. 
Take the result and divide it by the "does not close" distance (2 cun), halving it as the divisor. 
Take the result and add half of the "does not close" distance. This gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

# 去閫一尺
去閫 = 1  # in chi

# 不合二寸
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘，所得
平方 = 去閫 * 去閫

# 以不合二寸半之而一，所得
半不合 = 不合 / 2
商 = 平方 / 半不合

# 增不合之半，即得門廣
門廣 = 商 + 半不合

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # Convert chi to zhang#----- content ends here -----

"""
"""
