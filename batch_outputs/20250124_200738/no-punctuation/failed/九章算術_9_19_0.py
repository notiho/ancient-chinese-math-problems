"""
今有邑方不知大小各中開門出北門二十步有木出南門十四步折而西行一千七百七十五步見木問邑方幾何
術曰以出北門步數乘西行步數倍之為實并出南門步數為從法開方除之即邑方
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a square city whose size is unknown. 
From the center of the city, a gate opens to the north. Walking 20 bu north, there is a tree. 
Walking 14 bu south from the center, and then turning west to walk 1775 bu, there is the same tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of steps north of the gate by the number of steps west, and double it, obtaining the dividend.
Add the number of steps south of the gate, obtaining the divisor.
Extract the square root of the quotient, and this is the side length of the square city.

The answer says: *a* bu.
"""

from fractions import Fraction
from math import isqrt

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
a = isqrt(Fraction(實, 法))  # Using integer square root for exactness

a#----- content ends here -----

"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
