"""
今有粟四斗，欲為熟菽。問︰得幾何？
荅曰：為熟菽 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 4 dou of millet. It is desired to turn it into cooked beans.
Question: how much cooked beans does it make?

Answer: it makes *a* dou of cooked beans.
"""

# 粟四斗
粟 = 4

# Conversion ratio: 1 dou of millet produces 3 dou of cooked beans
conversion_ratio = Fraction(3, 1)

# Calculate the amount of cooked beans
a = 粟 * conversion_ratio

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 12"""
