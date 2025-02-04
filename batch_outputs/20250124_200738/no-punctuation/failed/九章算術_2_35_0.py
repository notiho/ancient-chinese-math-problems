"""
今有出錢二千三百七十買布九匹二丈七尺欲匹率之問匹幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一匹 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
Question: how much does one bolt cost on average?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Use the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the cost of one bolt.

Answer: one bolt costs *a* qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹
匹數 = 9

# 每匹二丈七尺
每匹布長 = 2 * 10 + 7  # Convert zhang to chi (1 zhang = 10 chi)

# 所買率為法
所買率 = 匹數 * 每匹布長

# 所求率為一匹布
所求率 = 每匹布長

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 實如法得一
a = Fraction(實, 所買率)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/3"""
