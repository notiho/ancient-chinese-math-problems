"""
今有絹積尺一萬三千四百六十三尺五寸四分問為匹幾何
術曰先置積尺數以匹四十尺為法除之即得
答曰 a匹 b丈
"""

"""
Suppose there is a total of 13,463 chi, 5 cun, and 4 fen of silk.
Question: how many pi (bolts of silk) does it make?

The procedure says: First, place the total number of chi.
Use 40 chi per pi as the divisor.
Divide by this, and the result is obtained.

Answer: it makes *a* pi and *b* zhang.
"""

from fractions import Fraction

# 絹積尺一萬三千四百六十三尺五寸四分
積尺 = 13463 + Fraction(5, 10) + Fraction(4, 100)

# 匹四十尺為法
法 = 40

# 以匹四十尺為法除之即得
a = 積尺 // 法  # Number of full pi
b = 積尺 % 法  # Remaining chi (in zhang)

# Convert remaining chi to zhang (1 zhang = 10 chi)
b = Fraction(b, 10)  # Remaining in zhang
"""
"""
