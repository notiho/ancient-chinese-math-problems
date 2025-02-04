"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, worth 125 qian. 
Now, there is 2 zhang and 7 chi of cloth. 
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Multiply the number of chi in the current cloth by the price of one bolt to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

from fractions import Fraction

# 布一匹，價直一百二十五
匹價 = 125

# 一匹尺數 (1 匹 = 4 丈)
匹尺數 = 4 * 10  # 1 丈 = 10 尺

# 今有布二丈七尺
布丈 = 2
布尺 = 7
布總尺數 = 布丈 * 10 + 布尺

# 今有布尺數乘價錢為實
實 = 布總尺數 * 匹價

# 實如法得錢數
a = Fraction(實, 匹尺數)

# Output the result
a  # a錢#----- content ends here -----

"""
"""
