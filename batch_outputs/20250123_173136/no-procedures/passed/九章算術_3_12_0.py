"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
荅曰： a錢 。
"""

"""
Suppose there is one bolt of cloth worth 125 qian. Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

# 布一匹價直一百二十五
匹價 = 125

# 一匹布的長度 (1匹 = 4丈)
匹長 = 4

# 布二丈七尺
布長 = 2 + Fraction(7, 10)  # 1丈 = 10尺

# 計算每丈的價值
每丈價值 = 匹價 / 匹長

# 計算布二丈七尺的價值
a = 布長 * 每丈價值

a
"""
"""
