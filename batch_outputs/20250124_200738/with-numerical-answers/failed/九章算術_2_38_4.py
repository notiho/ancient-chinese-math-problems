"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=34/15)鈞 ，斤 b(=5)錢 。其 c(=13/12)石 ，斤 d(=6)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 1120 qian to buy 1 shi, 2 jun, and 18 jin of silk.
It is desired to determine the price per jin according to its value.
Question: what is the price per jin for each unit?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the price per jin.
If the divisor is not satisfied, subtract the divisor from the dividend. The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The price per jun is *a*(=34/15) qian, and the price per jin is *b*(=5) qian.
The price per shi is *c*(=13/12) qian, and the price per jin is *d*(=6) qian.
"""

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 各置所買石、鈞、斤以為法
法石 = 石
法鈞 = 鈞
法斤 = 斤

# 以所率乘錢數為實
實石 = 錢數 * 石
實鈞 = 錢數 * 鈞
實斤 = 錢數 * 斤

# 實如法而一
a = Fraction(實鈞, 法鈞)  # 34/15 鈞
b = Fraction(實斤, 法斤)  # 5 錢
c = Fraction(實石, 法石)  # 13/12 石
d = Fraction(實斤, 法斤)  # 6 錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 1120
Variable 'b' has wrong value. Expected: 5, Actual: 1120
Variable 'c' has wrong value. Expected: 13/12, Actual: 1120
Variable 'd' has wrong value. Expected: 6, Actual: 1120"""
