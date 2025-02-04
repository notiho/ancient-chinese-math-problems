"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤石率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 石 b錢 其 c石 石 d錢 
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
Question: What is the price per shi and the price per jun?

The procedure says: Place the quantities of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the respective rates to form the dividend.
Divide the dividend by the divisor to find the rate.
If the remainder is less than the divisor, subtract the remainder from the divisor.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per jun is *a* qian per shi and *b* qian. The price per shi is *c* qian per shi and *d* qian.
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

# 各置所買石鈞斤兩以為法
法 = 石 * 1200 + 鈞 * 100 + 斤 * 16 + 兩 * 1 + Fraction(銖, 24)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每石率 = Fraction(實, 法)

# 不滿法者反以實減法
每鈞率 = 每石率 * 100  # Convert to per jun

# Answer
a = 每鈞率.numerator
b = 每鈞率.denominator
c = 每石率.numerator
d = 每石率.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 3048000
Variable 'b' has wrong value. Expected: 8051, Actual: 4039
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 30480
Variable 'd' has wrong value. Expected: 8052, Actual: 4039"""
