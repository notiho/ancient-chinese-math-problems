"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
- Seven families together contribute 190, which is 330 short.
- Nine families together contribute 270, which is 30 more than needed.

Question: What is the number of families (*a*) and the price of the cow (*b*)?

The procedure for surplus and deficit says:
1. Place the contribution rates (amounts contributed by each family) and write the surplus and deficit below them.
2. Multiply the contribution rates by their respective family counts, then sum them to obtain the dividend.
3. Add the surplus and deficit to obtain the divisor.
4. Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
5. For the surplus and deficit cases involving the same item being purchased:
   - Place the contribution rates.
   - Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
   - The dividend will be the price of the item, and the divisor will be the number of families.

Answer: *a* families, cow price *b*.
"""

from fractions import Fraction

# Given data
七家出 = 190  # Contribution by 7 families
七家不足 = 330  # Deficit for 7 families
九家出 = 270  # Contribution by 9 families
九家盈 = 30  # Surplus for 9 families

# Step 1: Multiply the contribution rates by their respective family counts
實 = (七家出 * 9) + (九家出 * 7)

# Step 2: Add the surplus and deficit
法 = 七家不足 + 九家盈

# Step 3: Divide the dividend by the divisor to find the number of families
家數 = Fraction(實, 法)

# Step 4: Subtract the smaller rate from the larger rate
餘 = abs(九家出 - 七家出)

# Step 5: Simplify to find the price of the cow
牛價 = Fraction(實, 法) * 餘 / 法

# Final answer
a = 家數
b = 牛價

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 10
Variable 'b' has wrong value. Expected: 3750, Actual: 20/9"""
