"""
今有出錢九百八十買矢簳五千八百二十枚欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a枚  b枚 一錢 其 c枚  d枚 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 980 qian to purchase 5820 arrows and shafts.
It is desired to know the rates of their respective prices (expensive and cheap).
Question: how many of each are there per qian?

The procedure for reversing the rates says: Take the total amount of money as the divisor.
Take the total number of items as the dividend.
Divide the dividend by the divisor, obtaining the base rate.
If the base rate is not an integer, reverse it by subtracting the remainder from the divisor.
If the divisor is smaller and the dividend is larger, multiply the divisor and dividend by the respective amounts of the two items.
This gives the number of each item.

Answer: *a* arrows and *b* shafts per qian for one rate, and *c* arrows and *d* shafts per qian for the other rate.
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
基準率 = Fraction(實, 法)

# 不滿法者反，以實減法
餘數 = 實 % 法
反法 = 法 - 餘數

# 法少實多，二物各以所得多少之數乘法實
貴率 = Fraction(實, 反法)
賤率 = Fraction(實, 法)

# 計算每錢的矢和簳數
a = 貴率.numerator
b = 貴率.denominator
c = 賤率.numerator
d = 賤率.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 97
Variable 'b' has wrong value. Expected: 5, Actual: 1
Variable 'c' has wrong value. Expected: 5520, Actual: 291
Variable 'd' has wrong value. Expected: 6, Actual: 49"""
