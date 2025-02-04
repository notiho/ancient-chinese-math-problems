"""
今有出錢二千三百七十買布九匹二丈七尺欲匹率之問匹幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一匹 a錢
"""

"""
Suppose there is an expenditure of 2370 qian to buy 9 bolts of cloth, each bolt being 2 zhang and 7 chi in length.
Question: how much does one bolt cost on average?

The procedure says: Multiply the desired rate (1 bolt) by the total money spent to obtain the dividend.
Take the rate of what was purchased (9 bolts × 2 zhang 7 chi) as the divisor.
Divide the dividend by the divisor to obtain the cost of one bolt.

Answer: one bolt costs *a* qian.
"""

# 出錢二千三百七十
錢數 = 2370

# 買布九匹
匹數 = 9

# 每匹二丈七尺
每匹布長 = 2 * 10 + 7  # Convert 2 zhang 7 chi to chi (1 zhang = 10 chi)

# 所買率為法
所買率 = 匹數 * 每匹布長

# 所求率為 1 匹，乘錢數為實
所求率 = 1
實 = 所求率 * 錢數

# 實如法得一
a = Fraction(實, 所買率)
"""
Variable 'a' has wrong value. Expected: 31600/129, Actual: 790/81"""
