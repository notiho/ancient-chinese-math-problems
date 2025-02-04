"""
今有素一匹一丈價直六百二十五今有錢五百問得素幾何
術曰以價直為法以一匹一丈尺數乘今有錢數為實實如法得素數
荅曰得素 a匹 
"""

#----- content starts here -----
"""
Suppose there is one bolt of silk, measuring 1 zhang, with a value of 625 coins.
Now, there are 500 coins available.
Question: how much silk can be obtained?

The procedure says: Take the value as the divisor.
Take the number of chi in one bolt of silk (1 zhang = 10 chi) and multiply it by the number of coins available, making the dividend.
Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a* bolts of silk.
"""

# 一匹一丈價直六百二十五
價直 = 625

# 一匹一丈尺數 (1丈 = 10尺)
匹丈尺數 = 10

# 今有錢五百
錢數 = 500

# 以一匹一丈尺數乘今有錢數，為實
實 = 匹丈尺數 * 錢數

# 以價直為法，實如法得素數
a = Fraction(實, 價直)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
