"""
今有堢壔方四丈髙二丈欲以塼四靣單壘之塼一枚廣五寸長一尺一寸厚二寸問用磚㡬何
術曰置堢壔方丈寸數以塼廣增之而以四乗之以髙乗之為實以塼長厚相乗為法實如法而一
答曰 a磚
"""

#----- content starts here -----
"""
Suppose there is a square wall base with a side length of 4 zhang and a height of 2 zhang. 
It is desired to cover all four sides of the wall base with bricks in a single layer.
Each brick has a width of 5 cun, a length of 1 chi 1 cun, and a thickness of 2 cun.
Question: how many bricks are needed?

The procedure says: Place the square wall base's side length in zhang, converted to cun.
Add the brick's width to it, then multiply it by 4.
Multiply the result by the height of the wall base, obtaining the dividend.
Multiply the brick's length and thickness together, obtaining the divisor.
Divide the dividend by the divisor, obtaining the number of bricks.

Answer: *a* bricks.
"""

# 堢壔方四丈
方長 = 4  # in zhang

# 高二丈
高 = 2  # in zhang

# 磚一枚廣五寸，長一尺一寸，厚二寸
磚廣 = 5  # in cun
磚長 = 10 + 1  # 1 chi = 10 cun, so 1 chi 1 cun = 11 cun
磚厚 = 2  # in cun

# 置堢壔方丈寸數
方長寸 = 方長 * 100  # 1 zhang = 10 chi = 100 cun

# 以塼廣增之
方長增 = 方長寸 + 磚廣

# 而以四乘之
四面周長 = 4 * 方長增

# 以高乘之為實
實 = 四面周長 * (高 * 100)  # Convert height to cun

# 以塼長厚相乘為法
法 = 磚長 * 磚厚

# 實如法而一
a = Fraction(實, 法)  # Number of bricks needed#----- content ends here -----

"""
"""
