"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
荅曰： a錢 。
"""

"""
Suppose there is one bolt of cloth worth 125 qian. Now, there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

# 1 匹布 = 1 丈
布一匹 = 1  # in 丈
價值一匹 = 125  # in 錢

# 布二丈七尺
布長度 = 2 + Fraction(7, 10)  # Convert 7 尺 to 丈 (1 丈 = 10 尺)

# Calculate the value of the given cloth
a = 布長度 * (價值一匹 / 布一匹)  # Value is proportional to length
"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 337.5"""
