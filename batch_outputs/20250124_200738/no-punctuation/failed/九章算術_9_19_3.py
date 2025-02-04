"""
今有邑方不知大小各中開門出北門二十步有木出南門十四步折而西行一千七百七十五步見木問邑方幾何
術曰以出北門步數乘西行步數倍之為實并出南門步數為從法開方除之即邑方
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a square city whose size is unknown. 
From the center, a gate opens to the north, and walking 20 bu north, there is a tree.
From the center, a gate opens to the south, and walking 14 bu south, then turning west and walking 1775 bu, there is another tree.
Question: what is the side length of the square city?

The procedure says: Multiply the number of bu walked north of the north gate by the number of bu walked west, and double it, obtaining the dividend.
Add the number of bu walked south of the south gate, obtaining the divisor.
Extract the square root of the division, and this is the side length of the square city.

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
a = math.sqrt(Fraction(法))

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 250, Actual: 266.4845211264624"""
