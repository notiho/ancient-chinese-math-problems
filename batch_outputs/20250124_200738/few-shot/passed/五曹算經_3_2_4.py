"""
今有粟五百六十斛。問：為糳米㡬何？
術曰：列粟五百六十斛，以二十四乘之得一萬三千四百四十斛，以五十除之即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 560 hu of millet. 
Question: how much roughly husked millet does it make?

The procedure says: Place the 560 hu of millet, multiply it by 24, obtaining 13440 hu.
Divide it by 50, and the result is obtained.

Answer: *a* hu.
"""

# 粟五百六十斛
粟 = 560

# 以二十四乘之
實 = 24 * 粟

# 以五十除之即得
a = Fraction(實, 50)#----- content ends here -----

"""
"""
