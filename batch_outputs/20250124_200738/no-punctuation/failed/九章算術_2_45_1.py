"""
今有出錢九百八十買矢簳五千八百二十枚欲其貴賤率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a枚  b枚 一錢 其 c枚  d枚 一錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 980 qian to buy 5820 arrows and shafts. It is desired to know the respective rates of the expensive and cheap ones.
Question: how many of each type are there, and what are their rates?

The procedure for reversing the rates says: Take the total money as the divisor (法), and the total quantity as the dividend (實). 
Divide the dividend by the divisor, obtaining the base rate. 
If the base rate is not an integer, reverse the calculation: subtract the remainder from the divisor, and adjust the divisor and dividend accordingly. 
For the two types of items, multiply the adjusted divisor and dividend by the respective quantities to determine the count of each type.

Answer: *a* arrows and *b* shafts per qian for the expensive type, and *c* arrows and *d* shafts per qian for the cheap type.
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
調整法 = 法 - 餘數

# 法少實多，二物各以所得多少之數乘法實
貴物數 = Fraction(調整法, 法) * 實
賤物數 = 實 - 貴物數

# 計算每錢的矢簳數
a = 貴物數 // 錢數
b = 貴物數 % 錢數
c = 賤物數 // 錢數
d = 賤物數 % 錢數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 300, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 17460/49
Variable 'c' has wrong value. Expected: 5520, Actual: 5
Variable 'd' has wrong value. Expected: 6, Actual: 27620/49"""
