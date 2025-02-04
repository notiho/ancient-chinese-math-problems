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

# 一匹布的長度為 4 丈 (standard length of one bolt of cloth)
匹長 = 4  # 丈

# 現在的布長為 2 丈 7 尺
布長 = 2 + Fraction(7, 10)  # 1 丈 = 10 尺

# 計算價值
a = 布長 * 匹價 / 匹長  # 按比例計算價值

a
"""
"""
