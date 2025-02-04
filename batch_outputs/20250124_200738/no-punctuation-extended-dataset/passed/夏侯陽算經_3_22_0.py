"""
今有絹積尺一萬三千四百六十三尺五寸四分問為匹幾何
術曰先置積尺數以匹四十尺為法除之即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there is a total of 13,463 chi, 5 cun, and 4 fen of silk.
Question: how many pi (bolts of silk) does it make?

The procedure says: First, place the total number of chi.
Use 40 chi per pi as the divisor.
Divide by this, and the result is obtained.

Answer: it makes *a* pi.
"""

from fractions import Fraction

# 絹積尺一萬三千四百六十三尺五寸四分
積尺 = 13463  # 尺
積寸 = 5       # 寸
積分 = 4       # 分

# Convert everything to 尺 (1 尺 = 10 寸, 1 寸 = 10 分)
積尺 += Fraction(積寸, 10) + Fraction(積分, 100)

# 匹四十尺為法
法 = 40  # 每匹 40 尺

# 以匹四十尺為法除之即得
a = Fraction(積尺, 法)  # 匹數

a#----- content ends here -----

"""
"""
