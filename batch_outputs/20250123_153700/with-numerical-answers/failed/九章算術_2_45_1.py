"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a(=300)枚 ， b(=5)枚 一錢 其 c(=5520)枚 ， d(=6)枚 一錢
"""

"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows. It is desired to determine the rates of their respective prices (more expensive and cheaper arrows).
Question: how many of each type and at what rate?

The procedure for reversing the rates says: Take the total amount of money as the divisor, and the given rate as the dividend. Perform the division, obtaining the rate for one unit.
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger.
For the two items, multiply the obtained rate by the total number of items to determine the quantity of each.

Answer: *a*(=300) arrows at *b*(=5) arrows per qian, and *c*(=5520) arrows at *d*(=6) arrows per qian.
"""

# 出錢九百八十
錢數 = 980

# 買矢簳五千八百二十枚
矢簳總數 = 5820

# 貴賤率：5枚一錢，6枚一錢
貴率 = 5
賤率 = 6

# 反其率術：以錢數為法，所率為實
貴實 = Fraction(錢數, 貴率)
賤實 = Fraction(錢數, 賤率)

# 確定貴賤數量
a = 貴實  # 貴的箭數量
b = 貴率  # 貴的箭每錢數量
c = 賤實  # 賤的箭數量
d = 賤率  # 賤的箭每錢數量

# 總數檢查
assert a + c == 矢簳總數  # 確保總數正確
"""
Code error: """
