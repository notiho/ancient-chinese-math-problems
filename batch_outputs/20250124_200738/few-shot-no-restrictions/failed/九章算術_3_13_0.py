"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

#----- content starts here -----
"""
Suppose there is 1 pi (bolt) of silk, measuring 1 zhang in length, priced at 625 qian.
Now, with 500 qian, how much silk can be obtained?

The procedure says: Take the price as the divisor.
Multiply the length (in chi) of 1 pi of silk by the amount of money currently available, giving the dividend.
Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a* pi of silk.
"""

from fractions import Fraction

# 1匹1丈 (1 pi = 1 zhang = 10 chi)
匹長度 = 10  # in chi

# 價直六百二十五
價直 = 625  # in qian

# 今有錢五百
有錢 = 500  # in qian

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
實 = 匹長度 * 有錢

# 實如法得素數
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
