"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a(=1)匹 。
"""

"""
Suppose there is 1 pi of plain silk, with a length of 1 zhang, and its price is 625 qian.
Now, there are 500 qian. 
Question: how much plain silk can be obtained?

The procedure says: Take the price as the divisor.
Multiply the number of chi in 1 pi of 1 zhang by the current amount of qian to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a*(=1) pi of plain silk can be obtained.
"""

# 素一匹一丈
匹數 = 1
丈數 = 1

# 一丈尺數
一丈尺數 = 10  # 1 丈 = 10 尺

# 價直六百二十五
價直 = 625

# 今有錢五百
今有錢 = 500

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
實 = 匹數 * 一丈尺數 * 今有錢

# 實如法得素數
a = Fraction(實, 法)  # 1

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
