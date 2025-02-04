"""
今有堢壔方四丈髙二丈欲以塼四靣單壘之塼一枚廣五寸長一尺一寸厚二寸問用磚㡬何
術曰置堢壔方丈寸數以塼廣增之而以四乗之以髙乗之為實以塼長厚相乗為法實如法而一
答曰 a磚
"""

#----- content starts here -----
"""
Suppose there is a square wall base (堢壔) with a side length of 4 zhang and a height of 2 zhang. 
It is desired to cover all four sides of the wall base with bricks in a single layer.
Each brick has a width of 5 cun, a length of 1 chi 1 cun, and a thickness of 2 cun.
Question: how many bricks are needed?

The procedure says: Place the side length of the wall base in zhang converted to cun. 
Add the width of the brick to it, then multiply it by 4. 
Multiply this by the height of the wall base to obtain the dividend.
Multiply the length and thickness of the brick to obtain the divisor.
Divide the dividend by the divisor to obtain the number of bricks.

Answer: *a* bricks.
"""

# 堢壔方四丈
方長 = 4  # in zhang

# 高二丈
高 = 2  # in zhang

# 磚一枚廣五寸
磚廣 = 5  # in cun

# 長一尺一寸
磚長 = 10 + 1  # 1 chi = 10 cun, so 1 chi 1 cun = 11 cun

# 厚二寸
磚厚 = 2  # in cun

# 置堢壔方丈寸數 (convert 方長 to cun: 1 zhang = 100 cun)
方長寸 = 方長 * 100

# 以塼廣增之
方長增 = 方長寸 + 磚廣

# 而以四乘之
周長 = 4 * 方長增

# 以高乘之為實 (convert 高 to cun: 1 zhang = 100 cun)
高寸 = 高 * 100
實 = 周長 * 高寸

# 以塼長厚相乘為法
法 = 磚長 * 磚厚

# 實如法而一
a = Fraction(實, 法)  # Number of bricks#----- content ends here -----

"""
"""
