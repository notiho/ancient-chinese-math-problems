"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

#----- content starts here -----
To solve this problem, we need to calculate the price per unit weight (jin) for different weight units (shi, jun, jin). Here's the solution based on the procedure provided:

"""
Suppose there is an expenditure of 1120 qian to buy 1 shi, 2 jun, and 18 jin of silk.
It is desired to calculate the price per jin for each weight unit (shi, jun, jin).

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the respective rates to obtain the dividend.
Divide the dividend by the divisor to get the price per jin.
If the divisor is not fully divisible, subtract the remainder from the divisor. The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per jun is *a* qian per jin. The price per jin is *b* qian per jin. The price per shi is *c* qian per jin. The price per jin is *d* qian per jin.
"""

from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 1 石 = 120 斤, 1 鈞 = 30 斤
石斤 = 石 * 120
鈞斤 = 鈞 * 30
總斤 = 石斤 + 鈞斤 + 斤

# 計算每斤的價格
每斤價格 = Fraction(錢數, 總斤)

# 計算每鈞的價格
每鈞價格 = 每斤價格 * 30

# 計算每石的價格
每石價格 = 每斤價格 * 120

# 結果
a = 每鈞價格
b = 每斤價格
c = 每石價格
d = 每斤價格

# Output
a, b, c, d#----- content ends here -----

"""
Code error: unterminated string literal (detected at line 2) (<string>, line 2)"""
