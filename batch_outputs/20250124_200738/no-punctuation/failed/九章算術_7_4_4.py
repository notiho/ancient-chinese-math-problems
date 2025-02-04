"""
今有共買金人出四百盈三千四百人出三百盈一百問人數金價各幾何
兩盈兩不足術曰置所出率盈不足各居其下令維乘所出率以少減多餘為實兩盈兩不足以少減多餘為法實如法而一有分者通之
荅曰 a人 金價 b 
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
One group of 400 people contributes 400 wen each, and there is an excess of 3000 wen.
Another group of 3400 people contributes 300 wen each, and there is an excess of 100 wen.
Question: how many people are there in total, and what is the price of the gold?

The procedure for "two excesses and two deficits" says: 
Place the contribution rates and the excess/deficit amounts below each other.
Multiply the contribution rates by the corresponding group sizes.
Subtract the smaller result from the larger result, and the remainder becomes the dividend.
For the excess/deficit amounts, subtract the smaller from the larger, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.

The answer says: there are *a* people, and the price of the gold is *b* wen.
"""

# Group 1: 400 people, 400 wen each, excess of 3000 wen
group1_people = 400
group1_rate = 400
group1_excess = 3000

# Group 2: 3400 people, 300 wen each, excess of 100 wen
group2_people = 3400
group2_rate = 300
group2_excess = 100

# Multiply the contribution rates by the group sizes
group1_total = group1_people * group1_rate
group2_total = group2_people * group2_rate

# Subtract the smaller total from the larger total to get the dividend
實 = abs(group1_total - group2_total)

# Subtract the smaller excess from the larger excess to get the divisor
法 = abs(group1_excess - group2_excess)

# Divide the dividend by the divisor to get the total number of people
a = Fraction(實, 法)

# Calculate the price of the gold (total contribution divided by the total number of people)
b = group1_rate * group1_people - group1_excess

# Simplify the price of the gold per person
b = Fraction(b, a)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 8600/29
Variable 'b' has wrong value. Expected: 9800, Actual: 22765/43"""
