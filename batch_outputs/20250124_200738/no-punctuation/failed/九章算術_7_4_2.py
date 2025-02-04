"""
今有共買金人出四百盈三千四百人出三百盈一百問人數金價各幾何
兩盈兩不足術曰置所出率盈不足各居其下令維乘所出率以少減多餘為實兩盈兩不足以少減多餘為法實如法而一有分者通之
荅曰 a人 金價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying gold together. 
One group contributes 400 and has an excess of 3000, while another group contributes 300 and has an excess of 100.
Question: how many people are there, and what is the price of the gold?

The procedure for solving two excesses or two deficits says: 
Place the contribution rates and the excesses/deficits below them. 
Multiply the contribution rates by their respective excesses/deficits.
Subtract the smaller product from the larger product, and the remainder becomes the dividend.
Subtract the smaller contribution rate from the larger contribution rate, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the number of people. 
If there is a remainder, adjust it accordingly.

The answer says: there are *a* people, and the price of the gold is *b*.
"""

# Group 1: 出四百盈三千
出率1 = 400
盈1 = 3000

# Group 2: 出三百盈一百
出率2 = 300
盈2 = 100

# 維乘所出率，以少減多，餘為實
實 = (出率1 * 盈1) - (出率2 * 盈2)

# 兩盈兩不足，以少減多，餘為法
法 = 出率1 - 出率2

# 實如法而一
a = Fraction(實, 法)

# 金價 b = 出率1 / a
b = Fraction(出率1, a)  # Alternatively, b = 出率2 / a

a = a
b = b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 11700
Variable 'b' has wrong value. Expected: 9800, Actual: 4/117"""
