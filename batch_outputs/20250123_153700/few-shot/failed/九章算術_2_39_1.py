"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu. 
It is desired to calculate the price per shi (stone) and per jun (unit of weight). 
Question: what are the prices per shi and per jun?

The procedure for the rates says: Place the quantities of shi, jun, jin, and liang as the divisor. 
Multiply the total money by the respective rates to obtain the dividend. 
Divide the dividend by the divisor to obtain the result. 
If the divisor is not a whole number, subtract the divisor from the dividend to adjust the calculation. 
The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The price per jun is *a* qian, and the remainder is *b* qian. 
The price per shi is *c* qian, and the remainder is *d* qian.
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

# 各置所買石、鈞、斤、兩以為法
# 1 石 = 30 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
法 = (
    石 * 30 * 30 * 16 * 24
    + 鈞 * 30 * 16 * 24
    + 斤 * 16 * 24
    + 兩 * 24
    + 銖
)

# 求每鈞的價格
# 以所率乘錢數為實
實_鈞 = 錢數 * 30 * 16 * 24

# 實如法而一
每鈞價格 = Fraction(實_鈞, 法)
a = 每鈞價格.numerator // 每鈞價格.denominator  # 整數部分
b = 每鈞價格.numerator % 每鈞價格.denominator  # 餘數部分

# 求每石的價格
實_石 = 錢數 * 30 * 30 * 16 * 24
每石價格 = Fraction(實_石, 法)
c = 每石價格.numerator // 每石價格.denominator  # 整數部分
d = 每石價格.numerator % 每石價格.denominator  # 餘數部分
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 424
Variable 'b' has wrong value. Expected: 8051, Actual: 39544
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 12723
Variable 'd' has wrong value. Expected: 8052, Actual: 47913"""
