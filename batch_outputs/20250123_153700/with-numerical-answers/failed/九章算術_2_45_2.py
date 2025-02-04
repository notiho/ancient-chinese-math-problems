"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=300)枚 ， b(=5)枚 一錢 其 c(=5520)枚 ， d(=6)枚 一錢
"""

"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows. It is desired to determine the rates of the expensive and cheap arrows.
Question: how many of each?

The procedure for reversing the rates says: Take the total amount of money as the divisor, and the rates as the dividend. 
Divide the dividend by the divisor to obtain the result. 
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger. 
For the two items, multiply the total number of items by the resulting fractions of the divisor and dividend to determine the quantities of each.

Answer: *a*(=300) arrows at *b*(=5) arrows per qian, and *c*(=5520) arrows at *d*(=6) arrows per qian.
"""

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳總數 = 5820

# 貴賤率：5枚一錢，6枚一錢
貴率 = 5
賤率 = 6

# 以錢數為法
法 = 錢數

# 所率為實
實 = 貴率 - 賤率

# 實如法而一
貴分 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
賤分 = 1 - 貴分

# 二物各以所得多少之數乘法實，即物數
a = 矢簳總數 * 貴分  # 300枚
c = 矢簳總數 * 賤分  # 5520枚

# 貴賤率
b = 貴率  # 5枚一錢
d = 賤率  # 6枚一錢
"""
Variable 'a' has wrong value. Expected: 300, Actual: -291/49
Variable 'c' has wrong value. Expected: 5520, Actual: 285471/49"""
