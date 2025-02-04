"""
今有邑方不知大小，各中開門。出北門三十步有木，出西門七百五十步見木。問︰邑方幾何？
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a square city of unknown size. Each side of the city has a gate at its center.
From the north gate, walking 30 bu north, there is a tree.
From the west gate, walking 750 bu west, there is another tree.
Question: what is the side length of the square city?

Answer: the side length of the city is *a* li.
"""

# From the problem, we know:
# The distance from the center of the city to the north gate is half the side length of the city (let's call it x/2).
# Similarly, the distance from the center of the city to the west gate is also x/2.
# Using the Pythagorean theorem, we can calculate the side length of the city.

# Distance from the north gate to the tree
北門距離 = 30

# Distance from the west gate to the tree
西門距離 = 750

# Total distance from the center of the city to the north tree (half the side length + 30 bu)
北距離 = Fraction(1, 2) * x + 北門距離

# Total distance from the center of the city to the west tree (half the side length + 750 bu)
#----- content ends here -----

"""
Code error: name 'x' is not defined"""
