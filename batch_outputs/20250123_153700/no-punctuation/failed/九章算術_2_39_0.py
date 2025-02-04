"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤石率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 石 b錢 其 c石 石 d錢 
"""

"""
Suppose there is an expenditure of 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.
It is desired to calculate the price per shi and the price per jun.

The procedure says: Place the amounts of shi, jun, jin, and liang as the divisor.
Multiply the total money spent by the respective rates to form the dividend.
Divide the dividend by the divisor to calculate the price per unit.
If there is a remainder less than the divisor, subtract it from the divisor to adjust the calculation.
The divisor corresponds to the cheaper rate, and the dividend corresponds to the more expensive rate.

Answer: The price per jun is *a* qian per shi, and *b* qian per shi. The price per shi is *c* qian per shi, and *d* qian per shi.
"""

# 出錢 13,970
錢數 = 13970

# 絲重量：1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 各置所買石鈞斤兩以為法
法 = 石 * 1200 + 鈞 * 100 + 斤 * 16 + 兩 * 1 + Fraction(銖, 10)

# 以所率乘錢數為實
實 = 錢數

# 實如法而一
每單位價格 = Fraction(實, 法)

# 不滿法者反以實減法法賤實貴
a = 每單位價格  # Price per jun
b = 每單位價格  # Placeholder for further refinement
c = 每單位價格  # Price per shi
d = 每單位價格  # Placeholder for further refinement
"""
Variable 'a' has wrong value. Expected: 979/960, Actual: 27940/3703
Variable 'b' has wrong value. Expected: 8051, Actual: 27940/3703
Variable 'c' has wrong value. Expected: 68201/46080, Actual: 27940/3703
Variable 'd' has wrong value. Expected: 8052, Actual: 27940/3703"""
