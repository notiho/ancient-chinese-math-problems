"""
今有素一匹一丈價直六百二十五今有錢五百問得素幾何
術曰以價直為法以一匹一丈尺數乘今有錢數為實實如法得素數
荅曰得素 a匹 
"""

#----- content starts here -----
"""
Suppose there is a bolt of plain silk, 1 pi long and 1 zhang in length, valued at 625 coins.
Now, with 500 coins, how much silk can be obtained?

The procedure says: Take the value as the divisor.
Take the number of chi in 1 pi and 1 zhang, and multiply it by the current amount of money to get the dividend.
Divide the dividend by the divisor to get the amount of silk.

Answer: *a* pi of silk.
"""

# 一匹一丈價直六百二十五
價直 = 625

# 一匹一丈尺數 (1 zhang = 10 chi)
尺數 = 10

# 今有錢五百
錢數 = 500

# 以一匹一丈尺數乘今有錢數，為實
實 = 尺數 * 錢數

# 以價直為法
法 = 價直

# 實如法得素數
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
