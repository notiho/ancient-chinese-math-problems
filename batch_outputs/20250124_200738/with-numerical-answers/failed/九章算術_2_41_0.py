"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=18013/11520)石 ，斤 b(=67)錢 。其 c(=7897/384)斤 ，斤 d(=68)錢 。
"""

#----- content starts here -----
"""
Suppose there is 13,970 qian spent to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (jin rate) based on its value.
Question: what is the price per jin?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the rate by the amount of money to get the dividend.
Divide the dividend by the divisor to get the result.
If the dividend is less than the divisor, subtract the dividend from the divisor to adjust the calculation.
The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The price per shi is *a*(=18013/11520) qian. The price per jin is *b*(=67) qian.
The price per jin is *c*(=7897/384) qian. The price per jin is *d*(=68) qian.
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
法 = 石 * 120 + 鈞 * 10 + 斤 + Fraction(兩, 16) + Fraction(銖, 384)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
a = Fraction(實, 法)  # Price per shi
b = int(a * 120)  # Price per jin (rounded down)

# Adjusting for fractional jin
c = Fraction(實, 法 * 120)  # Fractional price per jin
d = int(c)  # Price per jin (rounded down)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 5364480/64589
Variable 'b' has wrong value. Expected: 67, Actual: 9966
Variable 'c' has wrong value. Expected: 7897/384, Actual: 44704/64589
Variable 'd' has wrong value. Expected: 68, Actual: 0"""
