"""
今有布一匹價直一百二十五今有布二丈七尺問得錢幾何
術曰以一匹尺數為法今有布尺數乘價錢為實實如法得錢數
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth worth 125 qian. Now, there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Now, take the number of chi in the cloth and multiply it by the price in qian, obtaining the dividend.
Divide the dividend by the divisor to get the amount of qian.

The answer says: *a* qian.
"""

# 一匹布的尺數
匹布長度 = 1 * 10 * 10  # 1 bolt = 10 zhang = 100 chi

# 一匹布的價值
匹布價值 = 125

# 現有布的長度 (2丈7尺)
布長度 = 2 * 10 + 7  # 2 zhang = 20 chi, plus 7 chi

# 以一匹尺數為法
法 = 匹布長度

# 現有布尺數乘價錢為實
實 = 布長度 * 匹布價值

# 實如法得錢數
a = Fraction(實, 法)  # The amount of qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 135/4"""
