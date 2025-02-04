"""
今有絲九两得絹一疋，有絲三百二十四斤。問：計得㡬何？
術曰：列三百二十四斤，以十六两乘之，得五千一百八十四两；以九两除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk required to produce 1 bolt of silk fabric (絹). 
Now, there are 324 jin of silk.
Question: how many bolts of silk fabric can be produced?

The procedure says: Multiply 324 jin by 16 to convert it into liang, obtaining 5184 liang.
Divide this by 9 liang to determine the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 絲九两得絹一疋
絲_per_疋 = 9  # 9 liang per bolt

# 絲三百二十四斤
絲_in_斤 = 324  # 324 jin

# 一斤等於十六两
兩_per_斤 = 16

# 將斤轉換為两
絲_in_兩 = 絲_in_斤 * 兩_per_斤  # 324 * 16 = 5184 liang

# 計算得疋數
a = Fraction(絲_in_兩, 絲_per_疋)  # 5184 / 9

# Output the result
a#----- content ends here -----

"""
"""
