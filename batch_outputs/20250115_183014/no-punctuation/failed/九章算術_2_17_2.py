"""
今有粟四斗欲為熟菽問得幾何
術曰以粟求熟菽二百七之百而一
荅曰為熟菽 a斗 
"""

"""
Suppose there are 4 dou of millet. It is desired to turn it into cooked beans.
Question: how much cooked beans does one obtain?

The procedure says: when seeking cooked beans using millet, multiply by 100 and divide by 207.

The answer says: it makes *a* dou of cooked beans.
"""

# 粟四斗
粟 = 4

# 以粟求熟菽，二百七之百而一
熟菽 = Fraction(100 * 粟, 207)

a = 熟菽
"""
Variable 'a' has wrong value. Expected: 207/25, Actual: 400/207"""
