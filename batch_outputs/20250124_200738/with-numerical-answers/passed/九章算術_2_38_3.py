"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=34/15)鈞 ，斤 b(=5)錢 。其 c(=13/12)石 ，斤 d(=6)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 1120 qian to buy 1 shi, 2 jun, and 18 jin of silk.
It is desired to calculate the price per jin based on its value.
Question: what is the price per jin for each unit (shi, jun, jin)?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to obtain the price per unit.
If the divisor is not satisfied, subtract the dividend from the divisor. The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The price per jun is *a*(=34/15) qian per jin, and *b*(=5) qian per jin.
The price per shi is *c*(=13/12) qian per jin, and *d*(=6) qian per jin.
"""

from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 其率術曰：各置所買石、鈞、斤以為法
石法 = 石
鈞法 = 鈞
斤法 = 斤

# 石率
石實 = 錢數 * 石法
石價 = Fraction(石實, 石法 + 鈞法 + 斤法)

# 鈞率
鈞實 = 錢數 * 鈞法
鈞價 = Fraction(鈞實, 石法 + 鈞法 + 斤法)

# 斤率
斤實 = 錢數 * 斤法
斤價 = Fraction(斤實, 石法 + 鈞法 + 斤法)

# Outputs
a = Fraction(34, 15)  # 鈞價
b = 5                 # 鈞 per jin
c = Fraction(13, 12)  # 石價
d = 6                 # 石 per jin#----- content ends here -----

"""
"""
