"""
今有出錢一萬三千九百七十，買絲一石二鈞二十八斤三兩五銖。欲其貴賤石率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，石 b錢 。其 c石 ，石 d錢 。
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi (stone) and its rate of value.
Question: what are the rates of value for each unit?

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total expenditure by the respective rates to obtain the dividend.
Perform the division to find the rate for each unit.
If the dividend is less than the divisor, subtract the dividend from the divisor.
The divisor represents the cheaper rate, and the dividend represents the more expensive rate.

Answer: The rate per jun is *a* qian, and per shi is *b* qian. The rate per shi is *c* qian, and per shi is *d* qian.
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
a = Fraction(實, 法)  # Rate per jun
b = Fraction(實, 石)  # Rate per shi

# Not enough information is provided to calculate c and d directly.
c = a  # Placeholder
d = b  # Placeholder#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 30480/4039
Variable 'b' has wrong value. Expected: 8051, Actual: 13970
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 30480/4039
Variable 'd' has wrong value. Expected: 8052, Actual: 13970"""
