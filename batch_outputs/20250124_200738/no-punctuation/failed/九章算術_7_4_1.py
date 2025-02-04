"""
今有共買金人出四百盈三千四百人出三百盈一百問人數金價各幾何
兩盈兩不足術曰置所出率盈不足各居其下令維乘所出率以少減多餘為實兩盈兩不足以少減多餘為法實如法而一有分者通之
荅曰 a人 金價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying gold. One group contributes 400 and has an excess of 3000. Another group contributes 300 and has an excess of 100.
Question: how many people are there, and what is the price of the gold?

The procedure for two excesses or two deficits says: Place the contribution rates and the excesses/deficits below each other.
Multiply the contribution rates by their respective excesses/deficits.
Subtract the smaller result from the larger result, and this becomes the dividend.
Subtract the smaller contribution rate from the larger contribution rate, and this becomes the divisor.
Divide the dividend by the divisor to obtain the number of people. If there is a remainder, simplify it.
The price of the gold is obtained by dividing the total contribution by the number of people.

Answer: *a* people, and the price of the gold is *b*.
"""

# Group 1: 出四百盈三千
出率1 = 400
盈1 = 3000

# Group 2: 出三百盈一百
出率2 = 300
盈2 = 100

# 令維乘所出率，以少減多，餘為實
實 = abs((出率1 * 盈1) - (出率2 * 盈2))

# 兩盈兩不足，以少減多，餘為法
法 = abs(出率1 - 出率2)

# 實如法而一，有分者通之
a = Fraction(實, 法)

# 金價 = 總出率 / 人數
總出率 = 出率1 * a - 盈1  # Using Group 1's data to calculate total contribution
b = Fraction(總出率, a)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 11700
Variable 'b' has wrong value. Expected: 9800, Actual: 15590/39"""
