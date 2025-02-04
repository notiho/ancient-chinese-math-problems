"""
今有開門去閫一尺不合二寸問門廣幾何
術曰以去閫一尺自乘所得以不合二寸半之而一所得增不合之半即得門廣
荅曰 a丈 
"""

#----- content starts here -----
"""
Suppose there is a door, with the distance from the door frame (去閫) being 1 chi, and the gap when the door is closed (不合) being 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the door frame (去閫, 1 chi) and square it.
Divide the result by half of the gap when the door is closed (不合, 2 cun), and add half of the gap.
This gives the width of the door.

Answer: the door is *a* zhang wide.
"""

# 去閫一尺
去閫 = 1  # in chi

# 不合二寸
不合 = Fraction(2, 10)  # convert cun to chi (1 chi = 10 cun)

# 以去閫一尺自乘所得
去閫平方 = 去閫 * 去閫

# 不合二寸半之而一
不合半 = 不合 / 2
商 = 去閫平方 / 不合半

# 所得增不合之半
門廣 = 商 + 不合半

# Convert to zhang (1 zhang = 10 chi)
a = Fraction(門廣, 10)  # in zhang#----- content ends here -----

"""
"""
