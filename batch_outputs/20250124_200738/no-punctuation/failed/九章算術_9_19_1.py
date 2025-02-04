"""
今有邑方不知大小各中開門出北門二十步有木出南門十四步折而西行一千七百七十五步見木問邑方幾何
術曰以出北門步數乘西行步數倍之為實并出南門步數為從法開方除之即邑方
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a square city whose size is unknown. A gate is opened in the middle of each side.
From the north gate, walking 20 bu, there is a tree.
From the south gate, walking 14 bu, then turning west and walking 1775 bu, there is the same tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of bu walked from the north gate by the number of bu walked westward, double it, and take it as the dividend.
Add the number of bu walked from the south gate to obtain the divisor.
Extract the square root of the quotient, and this is the side length of the square city.

The answer says: *a* bu.
"""

from fractions import Fraction
import math

# 出北門二十步
北門步數 = 20

# 出南門十四步
南門步數 = 14

# 西行一千七百七十五步
西行步數 = 1775

# 以出北門步數乘西行步數
實 = 北門步數 * 西行步數

# 倍之為實
實 = 2 * 實

# 并出南門步數為從法
法 = 實 + 南門步數

# 開方除之即邑方
a = math.sqrt(Fraction(實, 法))  # 開方 (square root)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 250, Actual: 0.9999014230287492"""
