"""
今有出錢九百八十買矢簳五千八百二十枚欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a枚  b枚 一錢 其 c枚  d枚 一錢
"""

#----- content starts here -----
"""
Suppose there is a total of 980 qian spent to buy 5820 arrows and shafts. It is desired to determine the rate of expensive and cheap ones.
Question: how many of each type are there, and what is the rate of each?

The procedure for reversing the rates says: Take the total amount of money as the divisor (法). Take the total number of items as the dividend (實). Divide the dividend by the divisor to get the base rate. If the divisor does not fully divide the dividend, reverse the calculation by subtracting the divisor from the dividend. When the divisor is smaller and the dividend is larger, multiply the divisor and dividend by the respective quantities of the two types to determine the number of each type.

Answer: *a* arrows and shafts for *b* qian each, and *c* arrows and shafts for *d* qian each.
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

# 不滿法者反以實減法
餘數 = 實 % 法
高價率 = 基準率 + 1 if 餘數 != 0 else 基準率
低價率 = 基準率

# 法少實多，二物各以所得多少之數乘法實
高價數 = 餘數
低價數 = 法 - 餘數

# 高價物數
高價物數 = 高價數 * 高價率

# 低價物數
低價物數 = 低價數 * 低價率

# 結果
a = 高價物數
b = 高價數
c = 低價物數
d = 低價數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 312800/49
Variable 'b' has wrong value. Expected: 5, Actual: 920
Variable 'c' has wrong value. Expected: 5520, Actual: 17460/49
Variable 'd' has wrong value. Expected: 6, Actual: 60"""
