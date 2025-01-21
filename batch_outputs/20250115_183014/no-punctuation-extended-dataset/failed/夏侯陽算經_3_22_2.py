"""
今有絹積尺一萬三千四百六十三尺五寸四分問為匹幾何
術曰先置積尺數以匹四十尺為法除之即得
答曰 a匹 b丈
"""

"""
Suppose there is a total of 13,463 chi, 5 cun, and 4 fen of silk.
Question: how many bolts (pi) does it make?

The procedure says: First, place the total number of chi.
Use 40 chi per bolt as the divisor.
Divide by this, and you will obtain the result.

Answer: *a* bolts and *b* chi.
"""

from fractions import Fraction

# 絹積尺一萬三千四百六十三尺五寸四分
積尺 = 13463 + Fraction(5, 10) + Fraction(4, 100)

# 匹四十尺為法
法 = 40

# 以匹四十尺為法除之即得
a = 積尺 // 法  # Number of full bolts (匹)
b = 積尺 % 法   # Remaining chi (丈) after full bolts
"""
Variable 'b' has wrong value. Expected: 1177/500, Actual: 1177/50"""
