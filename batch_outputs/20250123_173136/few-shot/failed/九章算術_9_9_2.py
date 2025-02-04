"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

"""
Suppose there is a door that is 1 chi away from the threshold and does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the threshold (1 chi) and square it. 
Take the result and divide it by the amount it does not close (2 cun), then divide by 2. 
Add half of the amount it does not close to the result, and this gives the width of the door.

Answer: *a* zhang.
"""

# 去閫一尺
去閫 = 1  # in chi

# 不合二寸
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘，所得
平方 = 去閫 * 去閫

# 以不合二寸半之而一，所得
商 = 平方 / 不合 / 2

# 增不合之半
門廣 = 商 + (不合 / 2)

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # Convert chi to zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 13/50"""
