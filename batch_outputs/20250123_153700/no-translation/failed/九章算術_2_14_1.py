"""
今有粟七斗五升、七分升之四，欲為稻。問︰得幾何？
術曰：以粟求稻，六之，五而一。
荅曰：為稻 a斗 。
"""


# 粟七斗五升、七分升之四
粟 = 7 * 10 + 5 + Fraction(4, 7)  # Convert to 升

# 以粟求稻，六之
稻 = 6 * 粟

# 五而一
稻 = Fraction(稻, 5)

# Convert back to 斗
a = Fraction稻, 10)
"""
Code error: unmatched ')' (<string>, line 13)"""
