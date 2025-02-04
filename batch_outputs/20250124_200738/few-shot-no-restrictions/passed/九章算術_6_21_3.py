"""
今有一人一日為牡瓦三十八枚，一人一日為牝瓦七十六枚。今令一人一日作瓦，牝、牡相半，問︰成瓦幾何？
術曰：并牝、牡為法，牝牡相乘為實，實如法得一枚。
荅曰： a枚 。
"""

#----- content starts here -----
"""
Suppose one person in one day makes 38 male tiles (牡瓦), and one person in one day makes 76 female tiles (牝瓦).
Now, let one person in one day make tiles such that male and female tiles are equal in number (half each).
Question: how many tiles are made in total?

The procedure says: Add the male and female tiles together to get the divisor.
Multiply the male and female tiles to get the dividend.
Divide the dividend by the divisor to get the number of tiles made in one day.

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
a = Fraction(實, 法)  # The total number of tiles made in one day

a#----- content ends here -----

"""
"""
