"""
今有絲九两得絹一疋，有絲三百二十四斤。問：計得㡬何？
術曰：列三百二十四斤，以十六两乘之，得五千一百八十四两；以九两除之即得。
答曰： a疋 。
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk required to make 1 bolt of silk fabric (絹).
There are 324 jin of silk available.
Question: how many bolts of silk fabric can be made?

The procedure says: Multiply the 324 jin by 16 to convert it into liang, obtaining 5184 liang.
Then divide this by 9 liang to determine the number of bolts.

Answer: *a* bolts.
"""

from fractions import Fraction

# 絲九两得絹一疋
絲每疋 = 9  # 9 liang per bolt

# 絲三百二十四斤
絲斤 = 324  # 324 jin

# 一斤等於十六两
兩每斤 = 16

# 將斤轉換為两
絲兩 = 絲斤 * 兩每斤

# 計算可得絹疋數
a = Fraction(絲兩, 絲每疋)

# Answer
a#----- content ends here -----

"""
"""
