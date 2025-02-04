"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

"""
Suppose there is one bolt of cloth, priced at 125 qian.
Now, there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Take the number of chi in the current cloth and multiply it by the price in qian, giving the dividend.
Divide the dividend by the divisor to obtain the amount of money.

Answer: *a* qian.
"""

# 布一匹，價直一百二十五
匹價 = 125

# 一匹尺數為法
匹尺數 = 1 * 10 * 10  # 1 bolt = 1 zhang = 10 chi * 10 (1 zhang = 10 chi)

# 今有布二丈七尺
布尺數 = 2 * 10 + 7  # 2 zhang = 20 chi, plus 7 chi

# 今有布尺數乘價錢為實
實 = 布尺數 * 匹價

# 實如法得錢數
a = Fraction(實, 匹尺數)
"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 135/4"""
