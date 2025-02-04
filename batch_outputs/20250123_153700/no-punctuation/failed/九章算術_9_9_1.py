"""
今有開門去閫一尺不合二寸問門廣幾何
術曰以去閫一尺自乘所得以不合二寸半之而一所得增不合之半即得門廣
荅曰 a丈 
"""

"""
Suppose there is a door, with a distance of 1 chi from the lintel (去閫), and it does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the lintel (去閫, 1 chi) and square it.
Divide the result by the "does not close" distance (不合, 2 cun), and then halve it.
Add half of the "does not close" distance to the result, and this gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

# 去閫一尺
去閫 = 1  # chi

# 不合二寸
不合 = Fraction(2, 10)  # Convert 2 cun to chi (1 chi = 10 cun)

# 以去閫一尺自乘所得
去閫平方 = 去閫 * 去閫

# 以不合二寸半之而一所得
半之而一 = Fraction(去閫平方, 不合) / 2

# 增不合之半
門廣 = 半之而一 + (不合 / 2)

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # Convert chi to zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 13/50"""
