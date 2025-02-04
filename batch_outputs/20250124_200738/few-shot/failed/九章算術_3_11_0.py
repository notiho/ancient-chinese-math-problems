"""
今有縑一丈價直一百二十八。今有縑一匹九尺五寸，問︰得錢幾何？
術曰：以一丈寸數為法，以價錢數乘今有縑寸數為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is a piece of silk 1 zhang long, valued at 128 qian.
Now there is a piece of silk 1 pi long, which is 9 chi and 5 cun.
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor.
Multiply the price in qian by the number of cun in the given silk, obtaining the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

# 一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法
一丈寸數 = 10 * 10  # 1 zhang = 10 chi, and 1 chi = 10 cun, so 1 zhang = 100 cun

# 今有縑一匹九尺五寸
縑長度 = 9 * 10 + 5  # 9 chi = 90 cun, plus 5 cun = 95 cun

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 縑長度

# 實如法得錢數
a = Fraction(實, 一丈寸數)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
