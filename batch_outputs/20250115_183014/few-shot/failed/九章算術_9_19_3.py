"""
今有邑方不知大小，各中開門。出北門二十步有木。出南門十四步，折而西行一千七百七十五步見木。問︰邑方幾何？
術曰：以出北門步數乘西行步數，倍之，為實。并出南門步數為從法，開方除之，即邑方。
荅曰： a步 。
"""

"""
Suppose there is a square city, the size of which is unknown. Each side has a gate in the middle.
Exiting the north gate, walking 20 bu, there is a tree.
Exiting the south gate, walking 14 bu, then turning west and walking 1775 bu, there is the same tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of steps exiting the north gate by the number of steps walking west, and double it, obtaining the dividend.
Add the number of steps exiting the south gate to form the divisor.
Extract the square root of the result, and that is the side length of the square city.

Answer: *a* bu.
"""

# 出北門二十步
北門步數 = 20

# 出南門十四步
南門步數 = 14

# 西行一千七百七十五步
西行步數 = 1775

# 以出北門步數乘西行步數
實 = 北門步數 * 西行步數

# 倍之，為實
實 = 2 * 實

# 并出南門步數為從法
從法 = 南門步數

# 開方除之，即邑方
# 開方 (square root) is equivalent to raising to the power of 1/2
a = (實 / 從法) ** Fraction(1, 2)
"""
Variable 'a' has wrong value. Expected: 250, Actual: 71.21396331779725"""
