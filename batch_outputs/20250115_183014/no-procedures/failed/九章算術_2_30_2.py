"""
今有麥一斗，欲為大䵂。問︰得幾何？
荅曰：為大䵂 a斗 。
"""

"""
Suppose there is 1 dou of wheat. It is desired to turn it into "daqu" (a type of fermented grain product).
Question: how much "daqu" does it produce?

Answer: it produces *a* dou of "daqu."
"""

# 麥一斗
麥 = 1

# Conversion ratio: 1 dou of wheat produces 3 dou of "daqu" for every 5 dou of wheat
a = Fraction(3 * 麥, 5)

# Result
a
"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 3/5"""
