"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 980 qian to purchase 5820 arrows. It is desired to determine the rates of their relative value (expensive and cheap arrows). 
Question: what are the rates of the expensive and cheap arrows?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法). Take the total number of arrows as the dividend (實). Divide the dividend by the divisor to obtain the rate. If the dividend is not divisible by the divisor, subtract the remainder from the divisor. The divisor decreases, and the dividend increases. 
For the two types of arrows, multiply the divisor and dividend by the respective quantities to determine the number of each type.

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
每錢矢簳數 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
# Since the division is exact, no adjustment is needed here.

# 二物各以所得多少之數乘法實，即物數
# For simplicity, assume the expensive arrows are 1 per qian and the cheap arrows are the remainder.
貴箭每錢 = 1
貴箭數 = 法 * 貴箭每錢

賤箭每錢 = 每錢矢簳數 - 貴箭每錢
賤箭數 = 法 * 賤箭每錢

# Results
a = 貴箭數
b = 貴箭每錢
c = 賤箭數
d = 賤箭每錢#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 980
Variable 'b' has wrong value. Expected: 5, Actual: 1
Variable 'c' has wrong value. Expected: 5520, Actual: 4840
Variable 'd' has wrong value. Expected: 6, Actual: 242/49"""
