"""
今有共買羊人出五不足四十五人出七不足三問人數羊價各幾何
兩盈兩不足術曰置所出率盈不足各居其下令維乘所出率以少減多餘為實兩盈兩不足以少減多餘為法實如法而一有分者通之
荅曰 a人 羊價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying sheep. 
When each person contributes 5, they are short by 45.
When each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses and two deficits" says: 
Place the contribution rates (5 and 7), and the deficits (45 and 3) below each.
Multiply the contribution rates by their respective deficits, subtract the smaller product from the larger, and the remainder is the dividend.
Subtract the smaller deficit from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people. 
If there is a remainder, resolve it into a fraction.

Answer: *a* people, and the price of the sheep is *b*.
"""

# 人出五不足四十五
出率1 = 5
不足1 = 45

# 人出七不足三
出率2 = 7
不足2 = 3

# 維乘所出率，以少減多餘為實
實 = (出率2 * 不足2) - (出率1 * 不足1)

# 兩盈兩不足，以少減多餘為法
法 = 不足1 - 不足2

# 實如法而一
a = Fraction(實, 法)

# 羊價 = 人數 * 出率1 + 不足1
b = a * 出率1 + 不足1#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: -34/7
Variable 'b' has wrong value. Expected: 150, Actual: 145/7"""
