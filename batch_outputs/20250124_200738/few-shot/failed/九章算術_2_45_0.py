"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

#----- content starts here -----
"""
Suppose 980 qian (money) is spent to buy 5820 arrows. It is desired to determine the price rates for expensive and cheap arrows.
Question: how many arrows correspond to each rate?

The procedure for reversing the rate says: Take the amount of money as the divisor, and the total number of arrows as the dividend. Divide the dividend by the divisor, obtaining the unit rate.
If the dividend does not divide evenly into the divisor, subtract the remainder from the divisor. The divisor decreases, and the dividend increases.
For the two types of arrows, multiply the total number of arrows by the respective rates to determine the count of each type.

Answer: *a* arrows at *b* arrows per qian, and *c* arrows at *d* arrows per qian.
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
單位率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
餘數 = 實 % 法
if 餘數 != 0:
    法 = 法 - 餘數
    實 = 實 + 餘數

# 二物各以所得多少之數乘法實，即物數
貴箭率 = 法
賤箭率 = 法 + 1

貴箭數 = Fraction(實 * 貴箭率, 矢簳數)
賤箭數 = Fraction(實 * 賤箭率, 矢簳數)

a = 貴箭數
b = 貴箭率
c = 賤箭數
d = 賤箭率#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 6740/97
Variable 'b' has wrong value. Expected: 5, Actual: 60
Variable 'c' has wrong value. Expected: 5520, Actual: 20557/291
Variable 'd' has wrong value. Expected: 6, Actual: 61"""
