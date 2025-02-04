"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows at the base of the tree, spiraling around the tree 7 times and reaching the top of the tree.  
Question: how long is the vine?

Answer: the vine is *a* zhang long.
"""

from fractions import Fraction
import math

# 木長二丈 (tree height)
木長 = 2  # in zhang

# 圍之三尺 (circumference of the tree)
圍 = 3  # in chi

# 葛纏木七周 (vine spirals around the tree 7 times)
周數 = 7

# 葛長 (vine length) can be calculated using the Pythagorean theorem:
# Each spiral forms a right triangle with:
# - height = 木長 / 周數 (height of one spiral)
# - base = 圍 (circumference of the tree)

# Height of one spiral
單周高 = Fraction(木長 * 10, 周數)  # convert 木長 to chi (1 zhang = 10 chi)

# Length of one spiral (hypotenuse of the triangle)
單周長 = math.sqrt(單周高**2 + 圍**2)

# Total vine length
葛長 = 單周長 * 周數

# Convert the vine length back to zhang (1 zhang = 10 chi)
a = 葛長 / 10

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 2.8999999999999995"""
