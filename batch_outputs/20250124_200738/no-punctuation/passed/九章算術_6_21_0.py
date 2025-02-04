"""
今有一人一日為牡瓦三十八枚一人一日為牝瓦七十六枚今令一人一日作瓦牝牡相半問成瓦幾何
術曰并牝牡為法牝牡相乘為實實如法得一枚
荅曰 a枚 
"""

#----- content starts here -----
"""
Suppose one person in one day makes 38 male tiles (牡瓦), and one person in one day makes 76 female tiles (牝瓦).
Now, let one person in one day make tiles such that male and female tiles are equal in number.
Question: how many tiles are made in total?

The procedure says: Add the male and female tiles to form the divisor.
Multiply the male and female tiles to form the dividend.
Divide the dividend by the divisor to obtain the number of tiles made.

Answer: *a* tiles.
"""

# 一人一日為牡瓦三十八枚
牡瓦 = 38

# 一人一日為牝瓦七十六枚
牝瓦 = 76

# 并牝牡為法
法 = 牡瓦 + 牝瓦

# 牝牡相乘為實
實 = 牡瓦 * 牝瓦

# 實如法得一枚
a = Fraction(實, 法)#----- content ends here -----

"""
"""
