"""
今有絲九两得絹一疋有絲三百二十四斤問計得㡬何
術曰列三百二十四斤以十六两乘之得五千一百八十四两以九两除之即得
答曰 a疋 
"""

#----- content starts here -----
"""
Suppose there are 9 liang of silk required to make 1 bolt of silk fabric. 
If there are 324 jin of silk, how many bolts of fabric can be made?

The procedure says: Place the 324 jin, multiply it by 16 liang (since 1 jin = 16 liang), obtaining 5184 liang.
Divide this by 9 liang, and the result is the number of bolts.

Answer: *a* bolts.
"""

# 絲九两得絹一疋
絲每疋 = 9

# 絲三百二十四斤
絲斤 = 324

# 以十六两乘之，得总两
總兩 = 16 * 絲斤

# 以九两除之，即得
a = Fraction(總兩, 絲每疋)#----- content ends here -----

"""
"""
