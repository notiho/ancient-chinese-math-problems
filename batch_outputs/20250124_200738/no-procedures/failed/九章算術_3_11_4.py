"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is silk of 1 zhang (10 chi) worth 128 qian. Now there is silk of 1 pi (9 chi and 5 cun). 
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# 1丈價值128錢
價值_一丈 = 128
長度_一丈 = 10  # 1丈 = 10尺

# 縑一匹長度為9尺5寸 (convert to chi, 1尺 = 10寸)
長度_一匹 = 9 + Fraction(5, 10)

# 計算單位價格 (每尺價值)
單位價格 = Fraction(價值_一丈, 長度_一丈)

# 計算一匹的價值
a = 單位價格 * 長度_一匹

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
