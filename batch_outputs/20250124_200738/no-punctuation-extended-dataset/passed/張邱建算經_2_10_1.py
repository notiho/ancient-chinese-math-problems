"""
今有堢壔方四丈髙二丈欲以塼四靣單壘之塼一枚廣五寸長一尺一寸厚二寸問用磚㡬何
術曰置堢壔方丈寸數以塼廣增之而以四乗之以髙乗之為實以塼長厚相乗為法實如法而一
答曰 a磚
"""

#----- content starts here -----
"""
Suppose there is a square embankment with a side length of 4 zhang and a height of 2 zhang. 
It is desired to cover all four sides of the embankment with bricks in a single layer.
Each brick has a width of 5 cun, a length of 1 chi 1 cun, and a thickness of 2 cun.
Question: how many bricks are needed?

The procedure says: Place the square embankment's side length in zhang converted to cun.
Add the brick's width to it, then multiply it by 4.
Multiply this by the height of the embankment to get the volume of the surface to be covered.
Multiply the brick's length and thickness to get the divisor.
Divide the volume by the divisor to get the number of bricks.

Answer: *a* bricks.
"""

# 堢壔方四丈
方丈 = 4

# 高二丈
高丈 = 2

# 塼一枚廣五寸
磚廣 = 5

# 長一尺一寸 (convert to cun: 1 chi = 10 cun)
磚長 = 10 + 1

# 厚二寸
磚厚 = 2

# 置堢壔方丈寸數 (convert to cun: 1 zhang = 100 cun)
方寸 = 方丈 * 100

# 以塼廣增之
方寸增 = 方寸 + 磚廣

# 而以四乘之
四面長度 = 4 * 方寸增

# 以高乘之為實
實 = 四面長度 * (高丈 * 100)

# 以塼長厚相乘為法
法 = 磚長 *磚厚

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
