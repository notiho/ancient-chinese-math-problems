"""
今有一人一日為牡瓦三十八枚，一人一日為牝瓦七十六枚。今令一人一日作瓦，牝、牡相半，問︰成瓦幾何？
術曰：并牝、牡為法，牝牡相乘為實，實如法得一枚。
荅曰： a枚 。
"""

#----- content starts here -----
"""
Suppose one person in one day makes 38 male tiles, and one person in one day makes 76 female tiles.
Now, if one person in one day makes tiles, with male and female tiles being equal in number, how many tiles are made in total?

The procedure says: Add the male and female tiles together to form the divisor.
Multiply the male and female tiles together to form the dividend.
Divide the dividend by the divisor to obtain the number of tiles.

Answer: *a* tiles.
"""

# 一人一日為牡瓦三十八枚
牡瓦 = 38

# 一人一日為牝瓦七十六枚
牝瓦 = 76

# 并牝、牡為法
法 = 牡瓦 + 牝瓦

# 牝牡相乘為實
實 = 牡瓦 * 牝瓦

# 實如法得一枚
a = Fraction(實, 法)#----- content ends here -----

"""
"""
