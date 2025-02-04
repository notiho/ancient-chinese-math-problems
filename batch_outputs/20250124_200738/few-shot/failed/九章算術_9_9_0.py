"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door, with the distance from the door to the threshold being 1 chi, and the gap when the door is closed being 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the threshold (1 chi) and square it. 
Divide the result by the gap (2 cun), and then divide by 2.
Add half of the gap to the result, obtaining the width of the door.

Answer: the width of the door is *a* zhang.
"""

# 去閫一尺
去閫 = 1  # in chi

# 不合二寸
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# 以去閫一尺自乘，所得
自乘 = 去閫 * 去閫

# 以不合二寸半之而一，所得
半之而一 = 自乘 / 不合 / 2

# 增不合之半，即得門廣
門廣 = 半之而一 + (不合 / 2)

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # Convert chi to zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 13/50"""
