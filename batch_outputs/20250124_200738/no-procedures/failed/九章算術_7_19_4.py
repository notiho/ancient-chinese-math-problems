"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
荅曰：本 a錢 。利 b錢 。
"""

#----- content starts here -----
"""
Suppose someone holds a certain amount of money as capital and earns interest at a rate of 13%. 
They return the money in five installments: 
- First return: 14,000
- Second return: 13,000
- Third return: 12,000
- Fourth return: 11,000
- Fifth return: 10,000

After the five returns, both the principal and interest are fully paid. 
Question: What are the amounts of the principal (capital) and the interest?

Answer: The principal is *a* qian, and the interest is *b* qian.
"""

# 利率 (interest rate) is 13%, or 13/100
利率 = Fraction(13, 100)

# Returns in each installment
returns = [14000, 13000, 12000, 11000, 10000]

# Total amount returned
total_returned = sum(returns)

# Let the principal (capital) be "a" and the interest be "b"
# The total amount returned is equal to the principal plus the interest:
# total_returned = a + b
# The interest is calculated as: b = a * 利率
# Substituting b into the equation: total_returned = a + a * 利率
# Simplify: total_returned = a * (1 + 利率)

# Solve for "a" (the principal)
a = Fraction(total_returned, 1 + 利率)

# Solve for "b" (the interest)
b = a * 利率

# Results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 6000000/113
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 780000/113"""
