"""
今有菽二斗，欲為豉。問︰得幾何？
荅曰：為豉 a斗 。
"""

"""
Suppose there are 2 dou of beans (菽). It is desired to turn them into fermented beans (豉).
Question: how much fermented beans does it make?

Answer: it makes *a* dou of fermented beans.
"""

# 菽二斗
菽 = 2

# To make fermented beans, multiply by 3 and divide by 5
a = Fraction(3 * 菽, 5)

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 14/5, Actual: 6/5"""
