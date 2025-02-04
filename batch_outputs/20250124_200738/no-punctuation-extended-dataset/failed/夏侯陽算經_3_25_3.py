"""
今有絲一萬三千四百六十七兩問斤幾何
術曰置絲兩數四折半即是斤逢零六添之歸實
答曰 a斤
"""

#----- content starts here -----
"""
Suppose there are 13,467 liang of silk.
Question: how many jin does it make?

The procedure says: Place the number of liang of silk.
Divide it by 4 and a half (4.5), which gives the number of jin.
If there is a remainder of 6, add it to the result to finalize the calculation.

Answer: it makes *a* jin.
"""

# 絲一萬三千四百六十七兩
絲兩數 = 13467

# 四折半即是斤 (divide by 4.5)
a = Fraction(絲兩數, 9) * 2  # 4.5 is equivalent to 9/2, so we multiply by 2/9#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 13467/16, Actual: 8978/3"""
