"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money to trade, gaining a profit rate of 13%. Over five transactions, they return the following amounts:
- First return: 14,000
- Second return: 13,000
- Third return: 12,000
- Fourth return: 11,000
- Fifth return: 10,000

In total, the principal and profit are fully repaid.  
Question: What are the principal (original money held) and the total profit?

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

# 利率 (profit rate) is 13%
profit_rate = Fraction(13, 100)

# Returns from the five transactions
returns = [14000, 13000, 12000, 11000, 10000]

# Total amount returned
total_returned = sum(returns)

# Let the principal be `a` (unknown)
# Total profit is `b = a * profit_rate`
# Total returned = principal + profit = a + b = a + a * profit_rate = a * (1 + profit_rate)

# Solve for the principal `a`
a = Fraction(total_returned, 1 + profit_rate)

# Solve for the profit `b`
b = a * profit_rate

# Results
a, b 
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
