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
Take the number of chi in the current cloth and multiply it by the price of one bolt, giving the dividend.
Divide the dividend by the divisor to obtain the amount of money.

Answer: *a* qian.
"""

from fractions import Fraction

# 一匹布的尺數 (1匹 = 1丈 = 10尺)
一匹尺數 = 10

# 一匹布的價值
價值 = 125

# 現有布的長度 (2丈7尺 = 2 * 10 + 7 = 27尺)
布長度 = 2 * 10 + 7

# 計算實
實 = 布長度 * 價值

# 實如法得錢數
a = Fraction(實, 一匹尺數)

a  # 答案是 a錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 675/2"""
