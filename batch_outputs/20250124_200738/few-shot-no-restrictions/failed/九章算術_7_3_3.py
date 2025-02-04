"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
Seven families contribute a total of 190, which is 330 short of the required amount.
Nine families contribute a total of 270, which exceeds the required amount by 30.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below them respectively.
Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
For those sharing the same purchase, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify both the divisor and the dividend.
The dividend becomes the price of the item, and the divisor becomes the number of families.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# Known values
rate_7 = 190  # Contribution by 7 families
rate_9 = 270  # Contribution by 9 families
deficit = 330  # Amount short for 7 families
surplus = 30   # Amount over for 9 families

# Step 1: Multiply contribution rates by their respective surplus/deficit
dividend = (rate_7 * surplus) + (rate_9 * deficit)

# Step 2: Sum the surplus and deficit to form the divisor
divisor = surplus + deficit

# Step 3: Divide the dividend by the divisor to find the number of families
a = Fraction(dividend, divisor)

# Step 4: Calculate the price of the cow
# Use the contribution rate of 7 families and their deficit to find the price
b = Fraction(rate_7 + deficit, 7)

# Final answer
a = int(a)  # Number of families must be an integer
b = int(b)  # Price of the cow must be an integer

# Output
a, b
```#----- content ends here -----

"""
Code error: invalid syntax (<string>, line 46)"""
