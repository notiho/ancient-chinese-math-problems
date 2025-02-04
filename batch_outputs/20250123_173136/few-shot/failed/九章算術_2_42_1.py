"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per unit weight for both the higher and lower rates.
Question: what are the rates for each unit of weight?

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective unit to obtain the dividend.
Divide the dividend by the divisor to obtain the rate per unit.
If the dividend is less than the divisor, subtract the dividend from the divisor. The divisor represents the lower rate, and the dividend represents the higher rate.

Answer: The rate per shi is *a* qian, and the remainder is *b* qian. The rate per jun is *c* qian, and the remainder is *d* qian.
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

# 將重量轉換為統一單位（銖）
# 1 石 = 1200 斤, 1 鈞 = 100 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總銖 = 石 * 1200 * 16 * 24 + 鈞 * 100 * 16 * 24 + 斤 * 16 * 24 + 兩 * 24 + 銖

# 計算每石的價格
石法 = 石 * 1200 * 16 * 24
石實 = 錢數 * 石法
石率 = Fraction(石實, 總銖)
a = 石率.numerator // 石率.denominator  # 每石的整數部分
b = 石率.numerator % 石率.denominator  # 每石的餘數部分

# 計算每鈞的價格
鈞法 = 鈞 * 100 * 16 * 24
鈞實 = 錢數 * 鈞法
鈞率 = Fraction(鈞實, 總銖)
c = 鈞率.numerator // 鈞率.denominator  # 每鈞的整數部分
d = 鈞率.numerator % 鈞率.denominator  # 每鈞的餘數部分

# 答案
a石 = a
b錢 = b
c鈞 = c
d錢 = d
"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 11737
Variable 'b' has wrong value. Expected: 4, Actual: 464827
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 1956
Variable 'd' has wrong value. Expected: 5, Actual: 168876"""
