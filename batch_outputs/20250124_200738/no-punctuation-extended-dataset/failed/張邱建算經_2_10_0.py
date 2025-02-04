"""
今有堢壔方四丈髙二丈欲以塼四靣單壘之塼一枚廣五寸長一尺一寸厚二寸問用磚㡬何
術曰置堢壔方丈寸數以塼廣增之而以四乗之以髙乗之為實以塼長厚相乗為法實如法而一
答曰 a磚
"""

#----- content starts here -----
"""
Suppose there is a square wall foundation with a side length of 4 zhang and a height of 2 zhang.
It is desired to cover all four sides of the wall with single-layer bricks.
Each brick is 5 cun wide, 1 chi 1 cun long, and 2 cun thick.
Question: how many bricks are needed?

The procedure says: Place the square wall foundation's side length in zhang, converted to cun.
Add the width of the brick to it, and multiply it by 4.
Multiply this by the height, obtaining the volume.
Multiply the brick's length and thickness together, obtaining the divisor.
Divide the volume by the divisor, obtaining the number of bricks.

Answer: *a* bricks.
"""

# 堢壔方四丈
方長 = 4  # in 丈

# 高二丈
高 = 2  # in 丈

# 磚一枚廣五寸
磚廣 = 5  # in 寸

# 長一尺一寸
磚長 = 10 + 1  # 1 尺 = 10 寸, so 10 + 1 = 11 寸

# 厚二寸
磚厚 = 2  # in 寸

# 置堢壔方丈寸數
方長寸 = 方長 * 10  # 1 丈 = 10 尺, and 1 尺 = 10 寸, so 方長 in 寸

# 以塼廣增之
方長增 = 方長寸 + 磚廣

# 而以四乘之
周長 = 4 * 方長增

# 以高乘之為實
實 = 周長 * (高 * 10)  # 高 converted to 寸

# 以塼長厚相乘為法
法 = 磚長 * 磚厚

# 實如法而一
a = Fraction(實, 法)  # Number of bricks needed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 162000/11, Actual: 1800/11"""
