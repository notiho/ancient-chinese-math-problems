"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
荅曰：本 a錢 。利 b錢 。
"""

#----- content starts here -----
"""
Suppose someone holds a certain amount of money as capital and earns a profit of 13%. 
They return the money in five installments: 14,000, 13,000, 12,000, 11,000, and 10,000. 
After the fifth return, both the principal and the profit are fully repaid.

Question: What are the principal (capital) and the profit?

Answer: The principal is *a* qian, and the profit is *b* qian.
"""

# 利率 (profit rate) is 13%, or 13/100
profit_rate = Fraction(13, 100)

# Total amount returned
total_returned = 14000 + 13000 + 12000 + 11000 + 10000

# Let the principal be "a" and the profit be "b"
# Total returned = principal + profit
# Profit = principal * profit_rate
# So, total_returned = principal + (principal * profit_rate)
# total_returned = principal * (1 + profit_rate)

a = Fraction(total_returned, 1 + profit_rate)  # Principal
b = a * profit_rate  # Profit

# Results:
# a = principal
# b = profit#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
