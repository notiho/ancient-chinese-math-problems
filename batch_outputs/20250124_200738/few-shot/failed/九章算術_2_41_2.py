"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，斤 b錢 。其 c斤 ，斤 d錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk.
It is desired to calculate the price per jin (unit rate). Question: what is the price per jin?

The procedure for the rate says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total money by the rate to obtain the dividend.
Divide the dividend by the divisor to obtain the unit rate.
If the dividend does not fully divide the divisor, subtract the remainder from the divisor. The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: For *a* shi, the price per jin is *b* qian. For *c* jin, the price per jin is *d* qian.
"""

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石、鈞、斤、兩以為法
法 = (石 * 1200) + (鈞 * 100) + (斤 * 1) + (兩 / 16) + (銖 / (16 * 24))

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
斤率 = Fraction(實, 法)

# 不滿法者反以實減法，法賤實貴
a = 石
b = 斤率
c = 斤
d = 斤率#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
