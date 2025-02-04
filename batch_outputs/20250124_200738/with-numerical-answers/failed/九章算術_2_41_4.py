"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a(=18013/11520)石 ，斤 b(=67)錢 。其 c(=7897/384)斤 ，斤 d(=68)錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (pound) to determine its costliness or cheapness.
Question: what is the price per jin?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total money by the rate, obtaining the dividend.
Divide the dividend by the divisor, obtaining the price per jin.
If the dividend does not reach the divisor, subtract the divisor from the dividend.
The divisor represents cheapness, and the dividend represents costliness.

Answer: The price per *a*(=18013/11520) shi is 67 qian per jin.
The price per *c*(=7897/384) jin is 68 qian per jin.
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
# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
法 = (石 * 120) + (鈞 * 30) + 斤 + Fraction(兩, 16) + Fraction(銖, 16 * 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
a = Fraction(實, 法)  # Price per shi
b = int(a * 120)  # Price per jin in qian (rounded for shi)

c = a * 120  # Price per jin directly
d = int(c)  # Price per jin in qian (rounded for jin)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 5364480/79949
Variable 'b' has wrong value. Expected: 67, Actual: 8051
Variable 'c' has wrong value. Expected: 7897/384, Actual: 643737600/79949
Variable 'd' has wrong value. Expected: 68, Actual: 8051"""
