"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤石率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 石 b錢 其 c石 石 d錢 
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and the price per unit weight.

The procedure says: Place the weights (shi, jun, jin, liang, zhu) as the divisor.
Multiply the total money by the respective rates to form the dividend.
Divide the dividend by the divisor to calculate the price per unit weight.
If there is a remainder, subtract it from the divisor to adjust the calculation.

Answer: The price per jun is *a* qian per shi and *b* qian. The price per shi is *c* qian per shi and *d* qian.
"""

# 出錢 13,970 錢
錢數 = 13970

# 買絲重量：1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石鈞斤兩銖以為法
法 = (石 * 1200) + (鈞 * 100) + (斤 * 16) + (兩 * 1) + (銖 / 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每單位價格 = Fraction(實, 法)

# 計算每鈞的價格
每鈞價格 = 每單位價格 * 100

# 計算每石的價格
每石價格 = 每單位價格 * 1200

# 將結果分解為整數部分和餘數
a = 每鈞價格.numerator // 每鈞價格.denominator
b = 每鈞價格.numerator % 每鈞價格.denominator

c = 每石價格.numerator // 每石價格.denominator
d = 每石價格.numerator % 每石價格.denominator#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
