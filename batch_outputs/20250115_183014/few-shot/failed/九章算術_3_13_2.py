"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

"""
Suppose there is plain silk, 1 pi and 1 zhang in length, valued at 625 coins.
Now, there are 500 coins available.
Question: how much plain silk can be obtained?

The procedure says: Take the value as the divisor.
Take the number of chi in 1 pi and 1 zhang, and multiply it by the number of coins available, giving the dividend.
Do the division, obtaining the number of pi of silk.

Answer: *a* pi of silk can be obtained.
"""

# 素一匹一丈
一匹一丈尺數 = 1 * 10  # 1 pi = 10 chi

# 價直六百二十五
價直 = 625

# 今有錢五百
今有錢數 = 500

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
實 = 一匹一丈尺數 * 今有錢數

# 實如法得素數
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
