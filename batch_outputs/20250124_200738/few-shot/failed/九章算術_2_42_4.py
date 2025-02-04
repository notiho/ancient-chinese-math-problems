"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤兩率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a石 ，兩 b錢 。其 c鈞 ，兩 d錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per unit weight for both the expensive and cheap rates.
Question: what are the rates for each?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the respective rate to obtain the dividend.
Divide the dividend by the divisor to obtain the rate per unit.
If the dividend is less than the divisor, subtract the dividend from the divisor to determine the cheaper rate.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the expensive rate.

Answer: The expensive rate is *a* shi and *b* qian per unit. The cheaper rate is *c* jun and *d* qian per unit.
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
法 = 石 * 1200 + 鈞 * 100 + 斤 * 16 + 兩 * 1 + Fraction(銖, 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
貴率 = Fraction(實, 法)

# 不滿法者反以實減法，法賤實貴
賤率 = 法 - 貴率

# Convert 貴率 and 賤率 into shi and qian
a = 貴率.numerator // 1200  # 貴率 in 石
b = 貴率.numerator % 1200   # 貴率 remainder in 錢

c = 賤率.numerator // 1200  # 賤率 in 石
d = 賤率.numerator % 1200   # 賤率 remainder in 錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 12893/9216, Actual: 25
Variable 'b' has wrong value. Expected: 4, Actual: 480
Variable 'c' has wrong value. Expected: 3871/2880, Actual: 148931
Variable 'd' has wrong value. Expected: 5, Actual: 11"""
