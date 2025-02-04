"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""
Suppose there is a door, with the distance from the threshold to the door being 1 chi, and the gap when the door is closed being 2 cun.
Question: how wide is the door?

The procedure says: Square the distance from the threshold (1 chi), obtaining a result.
Divide this result by the gap (2 cun), halving it, and obtaining a result.
Add half of the gap to this result, and this gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

# 去閫一尺
去閫 = 1  # in chi

# 不合二寸
不合 = Fraction(2, 10)  # Convert cun to chi (1 chi = 10 cun)

# 以去閫一尺自乘，所得
去閫平方 = 去閫 * 去閫

# 以不合二寸半之而一，所得
商 = 去閫平方 / 不合

# 增不合之半
門廣 = 商 + (不合 / 2)

# Convert the result to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # Convert chi to zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 51/100"""
