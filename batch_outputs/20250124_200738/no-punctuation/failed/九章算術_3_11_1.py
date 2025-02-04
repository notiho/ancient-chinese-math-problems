"""
今有縑一丈價直一百二十八今有縑一匹九尺五寸問得錢幾何
術曰以一丈寸數為法以價錢數乘今有縑寸數為實實如法得錢數
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose there is a piece of silk 1 zhang long, valued at 128 qian. 
Now there is another piece of silk 1 pi long, which is 9 chi and 5 cun. 
Question: how much money is it worth?

The procedure says: Take the number of cun in 1 zhang as the divisor. 
Multiply the price in qian by the number of cun in the given silk to obtain the dividend. 
Divide the dividend by the divisor to get the amount of qian.

Answer: it is worth *a* qian.
"""

# 縑一丈價直一百二十八
一丈價 = 128

# 一丈寸數為法
一丈寸數 = 10 * 10  # 1 丈 = 10 尺, 1 尺 = 10 寸, so 1 丈 = 100 寸
法 = 一丈寸數

# 今有縑一匹九尺五寸
縑匹寸數 = 9 * 10 + 5  # 9 尺 = 90 寸, plus 5 寸

# 以價錢數乘今有縑寸數為實
實 = 一丈價 * 縑匹寸數

# 實如法得錢數
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3168/5, Actual: 608/5"""
