"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=18013/11520)石 ，斤 b(=67)錢 。其 c(=7897/384)斤 ，斤 d(=68)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (unit rate of price per weight).
Question: what is the price per jin?

The procedure for the rate says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the unit rate.
If the divisor does not divide evenly, subtract the remainder from the divisor. The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per shi is *a*(=18013/11520) qian, or 67 qian per jin for one rate.
The price per jin is *c*(=7897/384) qian, or 68 qian per jin for the other rate.
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

# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
總斤 = 石 * 120 + 鈞 * 30 + 斤 + Fraction(兩, 16) + Fraction(銖, 16 * 24)

# 各置所買石、鈞、斤、兩以為法
法 = 總斤

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
單價 = Fraction(實, 法)

# 不滿法者反以實減法，法賤實貴
a = Fraction(錢數, 石 * 120)  # Price per shi
b = int(單價)  # Cheaper rate (67 qian per jin)
c = 單價  # Exact price per jin (7897/384 qian)
d = int(單價) + 1  # More expensive rate (68 qian per jin)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 1397/12
Variable 'c' has wrong value. Expected: 7897/384, Actual: 5364480/79949"""
