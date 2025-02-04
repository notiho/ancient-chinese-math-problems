"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows. It is desired to determine the price rate for the expensive and cheap arrows.
Question: what is the price rate for each?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the total number of items as the dividend. Divide the dividend by the divisor, obtaining the rate. If the dividend is not divisible by the divisor, subtract the remainder from the divisor, making the divisor smaller and the dividend larger. For the two items, multiply the divisor and dividend by the respective quantities to determine the number of items.

Answer: *a* arrows at *b* arrows per qian, and *c* arrows at *d* arrows per qian.
"""

# 出錢九百八十
錢數 = 980

# 矢簳五千八百二十枚
矢簳數 = 5820

# 以錢數為法
法 = 錢數

# 所率為實
實 = 矢簳數

# 實如法而一
每錢矢數 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
餘數 = 矢簳數 % 錢數
if 餘數 != 0:
    法 -= 餘數
    實 += 餘數

# 二物各以所得多少之數乘法實，即物數
貴矢每錢 = 法
賤矢每錢 = 法 + 1

貴矢數 = (實 - 法) * 貴矢每錢
賤矢數 = 法 * 賤矢每錢

a = 貴矢數
b = 貴矢每錢
c = 賤矢數
d = 賤矢每錢
"""
Variable 'a' has wrong value. Expected: 300, Actual: 400800
Variable 'b' has wrong value. Expected: 5, Actual: 60
Variable 'c' has wrong value. Expected: 5520, Actual: 3660
Variable 'd' has wrong value. Expected: 6, Actual: 61"""
