"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 610 qian to buy 2100 feathers.
It is desired to determine the rates of their value (expensive and cheap).
Question: what are the rates for each?

The procedure for reversing the rates says: Take the amount of money as the divisor, and the amount of feathers as the dividend.
Divide the dividend by the divisor to obtain the rate.
If the dividend is less than the divisor, subtract the dividend from the divisor, making the divisor smaller and the dividend larger.
For the two types of items, multiply the respective quantities by the divisor and dividend to determine the number of items.

Answer: *a* feathers at *b* feathers per qian, and *c* feathers at *d* feathers per qian.
"""

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# 以錢數為法
法 = 錢數

# 所率為實
實 = 羽數

# 實如法而一
貴率 = Fraction(實, 法)

# 不滿法者反以實減法，法少，實多
便宜法 = 法 - 實
便宜實 = 實 - 法

# 二物各以所得多少之數乘法實，即物數
貴羽數 = 貴率 * 法
便宜羽數 = Fraction(便宜實, 便宜法)

# Assign results
a = 貴羽數
b = 貴率
c = 便宜羽數
d = Fraction(便宜法, 便宜實)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1140, Actual: 2100
Variable 'b' has wrong value. Expected: 3, Actual: 210/61
Variable 'c' has wrong value. Expected: 960, Actual: -1
Variable 'd' has wrong value. Expected: 4, Actual: -1"""
