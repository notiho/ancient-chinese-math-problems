"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
Suppose there is one bolt of cloth, valued at 125 qian.
Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Multiply the number of chi in the given cloth by the price in qian, obtaining the dividend.
Divide the dividend by the divisor, obtaining the amount of money.

Answer: *a* qian.
"""

# 一匹布的尺數 (1匹 = 4丈)
一匹布尺數 = 4 * 10  # 1丈 = 10尺

# 一匹布的價值
價值 = 125

# 今有布二丈七尺
布尺數 = 2 * 10 + 7  # 2丈7尺轉換為尺

# 以一匹尺數為法
法 = 一匹布尺數

# 今有布尺數乘價錢為實
實 = 布尺數 * 價值

# 實如法得錢數
a = Fraction(實, 法)
"""
"""
