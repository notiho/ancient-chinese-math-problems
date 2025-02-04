"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=300)枚 ， b(=5)枚 一錢 其 c(=5520)枚 ， d(=6)枚 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows. It is desired to determine the rates of their value, i.e., how many arrows are obtained per qian for the expensive and cheap rates.

The procedure for reversing the rates says: Take the total amount of money as the divisor, and the total number of arrows as the dividend. Divide the dividend by the divisor to obtain the base rate. If the dividend is not divisible by the divisor, subtract the remainder from the dividend, making the divisor smaller and the dividend larger. For the two types of goods, multiply the divisor and dividend by the respective quantities to determine the number of each type of good.

Answer: The expensive rate is *a*(=300) arrows, *b*(=5) arrows per qian. The cheap rate is *c*(=5520) arrows, *d*(=6) arrows per qian.
"""

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳數 = 5820

# 以錢數為法
法 = 錢數

# 所率為實
實 = 矢簳數

# 實如法而一
基本率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
貴率 = 5  # 貴的矢簳每錢 5 枚
賤率 = 6  # 賤的矢簳每錢 6 枚

# 二物各以所得多少之數乘法實，即物數
a = 貴率 * 法 // (貴率 + 賤率)  # 貴的矢簳數量
c = 賤率 * 法 // (貴率 + 賤率)  # 賤的矢簳數量

b = 貴率  # 貴的矢簳每錢數
d = 賤率  # 賤的矢簳每錢數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 445
Variable 'c' has wrong value. Expected: 5520, Actual: 534"""
