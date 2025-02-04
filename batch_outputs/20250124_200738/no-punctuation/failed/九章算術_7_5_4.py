"""
今有共買羊人出五不足四十五人出七不足三問人數羊價各幾何
兩盈兩不足術曰置所出率盈不足各居其下令維乘所出率以少減多餘為實兩盈兩不足以少減多餘為法實如法而一有分者通之
荅曰 a人 羊價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying sheep. 
When each person contributes 5, it is 45 short. 
When each person contributes 7, it is 3 over. 
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses and two deficits" says: 
Place the contribution rates, the excess, and the deficit, each below the other. 
Let them be multiplied by their respective contribution rates. 
Subtract the smaller from the larger, and the remainder is the dividend. 
For the divisor, subtract the smaller excess/deficit from the larger. 
Divide the dividend by the divisor, and the result is the number of people. 
If there is a remainder, convert it into a fraction.

The answer says: *a* people, and the price of the sheep is *b*.
"""

# 人出五不足四十五
出率1 = 5
不足1 = 45

# 人出七不足三
出率2 = 7
不足2 = -3  # Over is treated as negative deficit

# 令維乘所出率，以少減多餘為實
實 = abs((出率2 * 不足1) - (出率1 * 不足2))

# 兩盈兩不足，以少減多餘為法
法 = abs(不足1 - 不足2)

# 實如法而一
a = Fraction(實, 法)

# 羊價 b = 人數 * 出率1 + 不足1
b = a * 出率1 + 不足1#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: 55/8
Variable 'b' has wrong value. Expected: 150, Actual: 635/8"""
