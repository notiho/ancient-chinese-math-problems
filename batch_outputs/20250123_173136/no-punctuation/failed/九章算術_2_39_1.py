"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤石率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 石 b錢 其 c石 石 d錢 
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and the price per unit weight.

The procedure says: Place the weights (shi, jun, jin, liang, zhu) as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the price per unit weight.
If there is a remainder, subtract it from the divisor. The divisor gives the cheaper rate, and the dividend gives the more expensive rate.

Answer: The price per jun is *a* qian, and the remainder is *b* qian. The price per shi is *c* qian, and the remainder is *d* qian.
"""

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石鈞斤兩以為法
法 = 石 * 1200 + 鈞 * 100 + 斤 * 16 + 兩 * 1 + Fraction(銖, 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每單位價格 = Fraction(實, 法)

# 不滿法者反以實減法
整數部分 = 每單位價格.numerator // 每單位價格.denominator
餘數 = 每單位價格.numerator % 每單位價格.denominator

# 石率 (每石價格)
每石價格 = 整數部分
每石餘數 = 餘數

# 鈞率 (每鈞價格)
每鈞價格 = Fraction(每單位價格 * 100).numerator // Fraction(每單位價格 * 100).denominator
每鈞餘數 = Fraction(每單位價格 * 100).numerator % Fraction(每單位價格 * 100).denominator

a = 每鈞價格
b = 每鈞餘數
c = 每石價格
d = 每石餘數
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 754
Variable 'b' has wrong value. Expected: 8051, Actual: 2594
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 7
Variable 'd' has wrong value. Expected: 8052, Actual: 2207"""
