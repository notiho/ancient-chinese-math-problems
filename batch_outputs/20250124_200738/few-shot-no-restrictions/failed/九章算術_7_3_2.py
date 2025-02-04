"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
Seven families together contribute 190, which is 330 short. 
Nine families together contribute 270, which is 30 extra. 
Question: how many families are there, and what is the price of the cow?

The procedure for "excess and deficiency" says:
Place the contribution rates, and place the excess and deficiency below each. 
Multiply the contribution rates by their respective excess or deficiency, then sum them to obtain the dividend. 
Sum the excess and deficiency to obtain the divisor. 
Divide the dividend by the divisor to find the result. If there is a remainder, simplify it. 
For those who share the same purchased item, place the contribution rates, subtract the smaller from the larger, and reduce the remainder with the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# Given data
七家出 = 190  # Contribution by 7 families
七家不足 = 330  # Shortfall for 7 families
九家出 = 270  # Contribution by 9 families
九家盈 = 30  # Excess for 9 families

# Step 1: Place the contribution rates and excess/deficiency
七家率 = 7
九家率 = 9

# Step 2: Multiply contribution rates by their respective excess/deficiency
七家實 = 七家率 * 七家不足  # 7 * 330
九家實 = 九家率 * 九家盈  # 9 * 30

# Step 3: Sum the results to obtain the dividend
實 = 七家實 + 九家實  # Dividend

# Step 4: Sum the excess and deficiency to obtain the divisor
法 = 七家不足 + 九家盈  # Divisor

# Step 5: Divide the dividend by the divisor to find the number of families
a = Fraction(實, 法)  # Number of families

# Step 6: Calculate the price of the cow
# Subtract the smaller contribution rate from the larger
餘 = abs(九家率 - 七家率)

# Reduce the remainder with the divisor and dividend
b = Fraction(實, 餘)  # Price of the cow

# Final answer
a家 = a
b牛價 = b

a家, b牛價#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 43/6
Variable 'b' has wrong value. Expected: 3750, Actual: 1290"""
