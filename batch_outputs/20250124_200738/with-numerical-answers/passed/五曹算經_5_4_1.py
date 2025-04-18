"""
今有絲九两得絹一疋，有絲三百二十四斤。問：計得㡬何？
術曰：列三百二十四斤，以十六两乘之，得五千一百八十四两；以九两除之即得。
答曰： a(=576)疋 。
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk that produce 1 bolt of silk fabric.
Now, there are 324 jin of silk.
Question: how many bolts of silk fabric can be produced?

The procedure says: Place 324 jin, multiply it by 16 liang (since 1 jin = 16 liang), obtaining 5184 liang.
Divide it by 9 liang, and the result is the number of bolts of silk fabric.

Answer: *a*(=576) bolts.
"""

# 絲九两得絹一疋
絲每疋 = 9  # 9 liang per bolt

# 絲三百二十四斤
絲斤 = 324  # 324 jin

# 以十六两乘之，得五千一百八十四两
絲兩 = 16 * 絲斤  # Convert jin to liang (1 jin = 16 liang)

# 以九两除之即得
a = Fraction(絲兩, 絲每疋)  # 576 bolts#----- content ends here -----

"""
"""
