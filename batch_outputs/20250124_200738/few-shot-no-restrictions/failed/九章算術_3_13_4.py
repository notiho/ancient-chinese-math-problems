"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

#----- content starts here -----
"""
Suppose there is 1 pi of silk, measuring 1 zhang in length, and its price is 625 coins.
Now, there are 500 coins available.
Question: how much silk can be obtained?

The procedure says: Take the price as the divisor.
Multiply the length of 1 pi (in chi) by the number of coins available to get the dividend.
Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a* pi of silk.
"""

from fractions import Fraction

# 1匹1丈 (1 pi = 1 zhang = 10 chi)
匹長度 = 10  # in chi

# 價直六百二十五
價直 = 625  # in coins

# 今有錢五百
錢數 = 500  # in coins

# 以一匹一丈尺數乘今有錢數為實
實 = 匹長度 * 錢數

# 實如法得素數
a = Fraction(實, 價直)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
