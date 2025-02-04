"""
今有出錢九百八十買矢簳五千八百二十枚欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a枚  b枚 一錢 其 c枚  d枚 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows and shafts. It is desired to determine the rates of their respective values (expensive and cheap).
Question: how many of each type are there per qian?

The procedure for reversing the rates says: Take the total money as the divisor (法), and the total quantity as the dividend (實).
Divide the dividend by the divisor to find the base rate. If the result is not an integer, reverse the calculation by subtracting the dividend from the divisor.
When the divisor is smaller and the dividend is larger, multiply the divisor and dividend by the respective quantities of the two items to find their individual counts.

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
反法 = 法 - 實

# 法少實多，二物各以所得多少之數乘法實
a = 基準率.numerator
b = 基準率.denominator
c = 反法.numerator
d = 反法.denominator#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 291
Variable 'b' has wrong value. Expected: 5, Actual: 49
Variable 'c' has wrong value. Expected: 5520, Actual: -4840
Variable 'd' has wrong value. Expected: 6, Actual: 1"""
