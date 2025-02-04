"""
今有絹積尺一萬三千四百六十三尺五寸四分問為匹幾何
術曰先置積尺數以匹四十尺為法除之即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there is a total of 13,463 chi, 5 cun, and 4 fen of silk.
Question: how many bolts of silk does it make?

The procedure says: First, place the total number of chi.
Use 40 chi per bolt as the divisor.
Divide by this, and you obtain the number of bolts.

Answer: it makes *a* bolts.
"""

from fractions import Fraction

# 絹積尺一萬三千四百六十三尺五寸四分
積尺 = 13463 + Fraction(5, 10) + Fraction(4, 100)

# 匹四十尺為法
法 = 40

# 以匹四十尺為法除之，即得
a = Fraction(積尺, 法)#----- content ends here -----

"""
"""
