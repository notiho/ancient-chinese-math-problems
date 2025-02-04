"""
今有絲九两得絹一疋，有絲三百二十四斤。問：計得㡬何？
術曰：列三百二十四斤，以十六两乘之，得五千一百八十四两；以九两除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk that can produce 1 bolt of silk fabric (絹). 
Now, there are 324 jin of silk.
Question: how many bolts of silk fabric can be produced?

The procedure says: Take 324 jin, multiply it by 16 liang (since 1 jin = 16 liang), obtaining 5184 liang.
Divide this by 9 liang to get the result.

Answer: *a* bolts of silk fabric.
"""

from fractions import Fraction

# 絲九两得絹一疋
絲每疋 = 9  # 9 liang per bolt of silk fabric

# 絲三百二十四斤
絲斤 = 324  # 324 jin of silk

# 1斤 = 16两
絲两 = 絲斤 * 16  # Convert jin to liang

# 計算得疋數
a = Fraction(絲两, 絲每疋)

# Output the result
a#----- content ends here -----

"""
"""
