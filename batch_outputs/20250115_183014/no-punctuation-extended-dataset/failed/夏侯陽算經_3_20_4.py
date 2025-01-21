"""
今有布積尺一萬八千四百六十三尺四寸二分問為端幾何
術曰先置尺數以五十尺除之即得
答曰 a端
"""

"""
Suppose there is a total length of cloth measuring 18,463 chi, 4 cun, and 2 fen.
Question: how many duan (sections of 50 chi) does it make?

The procedure says: First, place the total number of chi. Divide it by 50 chi, and the result is obtained.

Answer: it makes *a* duan.
"""

from fractions import Fraction

# 布積尺一萬八千四百六十三尺四寸二分
尺 = 18463
寸 = 4
分 = Fraction(2, 10)  # 1 cun = 10 fen

# Convert everything to chi
總尺數 = 尺 + Fraction(寸, 10) + Fraction(分, 10)

# 以五十尺除之
每端尺數 = 50
a = 總尺數 / 每端尺數
"""
Variable 'a' has wrong value. Expected: 92250671/250000, Actual: 923171/2500"""
