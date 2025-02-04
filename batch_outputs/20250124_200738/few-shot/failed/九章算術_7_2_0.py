"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy a jade item. 
When each person contributes half the price, there is an excess of 4. 
When each person contributes less than half, there is a shortfall of 3. 
Question: how many people are there, and what is the price of the jade?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below them respectively. 
Multiply the contribution rates by their respective surplus or deficit, and sum these to form the dividend. 
Sum the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find 1 unit. 
If there is a fraction, simplify it. 
For cases where the surplus and deficit relate to the same item being purchased, 
place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a* people, and the price of the jade is *b*.
"""

# 盈四
盈 = 4

# 不足三
不足 = 3

# 人出半
所出率多 = Fraction(1, 2)

# 人出少半
所出率少 = Fraction(1, 2) - Fraction(1, 2)

# 置所出率，以少減多，餘
差 = 所出率多 - 所出率少

# 盈、不足各乘所出率，并以為實
實 = (所出率多 * 盈) + (所出率少 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 以約法、實
物價 = Fraction(實, 法)

# 實為物價，法為人數
人數 = Fraction(法, 差)

a = 人數
b = 物價#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 2/7"""
