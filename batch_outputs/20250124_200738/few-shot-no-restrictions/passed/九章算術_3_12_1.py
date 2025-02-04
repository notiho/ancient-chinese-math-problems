"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, valued at 125 qian.
Now there is a piece of cloth measuring 2 zhang and 7 chi.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Multiply the number of chi in the current piece of cloth by the price of one bolt, obtaining the dividend.
Divide the dividend by the divisor to obtain the amount of money.

Answer: *a* qian.
"""

# 一匹布的價值
匹價 = 125

# 一匹布的尺數 (1 匹 = 4 丈)
匹尺數 = 4 * 10  # 1 丈 = 10 尺

# 現有布的尺數 (2 丈 7 尺)
布尺數 = 2 * 10 + 7

# 今有布尺數乘價錢為實
實 = 布尺數 * 匹價

# 實如法得錢數
a = Fraction(實, 匹尺數)

a#----- content ends here -----

"""
"""
