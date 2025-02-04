"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a(=1)匹 。
"""

#----- content starts here -----
"""
Suppose there is plain silk, 1 pi and 1 zhang in length, with a value of 625 coins.
Now, there are 500 coins. 
Question: how much plain silk can be obtained?

The procedure says: Take the value as the divisor.
Multiply the number of chi in 1 pi and 1 zhang by the number of coins currently available, giving the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a*(=1) pi of plain silk can be obtained.
"""

# 素一匹一丈
匹 = 1
丈 = 1

# 一丈等於十尺
尺數 = 丈 * 10

# 價直六百二十五
價直 = 625

# 今有錢五百
錢數 = 500

# 以一匹一丈尺數乘今有錢數為實
實 = 尺數 * 錢數

# 實如法得素數
a = Fraction(實, 價直) # 1
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
