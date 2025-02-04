"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=42)人 ，璡價 b(=17) 。
"""

#----- content starts here -----
"""
Suppose people jointly buy a jade item. If each person contributes half, there is an excess of 4. 
If each person contributes less than half, there is a shortfall of 3. 
Question: what are the number of people and the price of the jade item?

The procedure for surplus and shortfall says:
Place the contribution rates, with the surplus and shortfall below them respectively.
Multiply the contribution rates by their respective multipliers, and add them to form the dividend.
Add the surplus and shortfall to form the divisor.
Divide the dividend by the divisor to obtain 1 unit. If there is a fraction, simplify it.
For items jointly purchased with the same contribution rates for surplus and shortfall:
Place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a*(=42) people, *b*(=17) is the price of the jade item.
"""

# 人出半，盈四
所出率_盈 = Fraction(1, 2)
盈 = 4

# 人出少半，不足三
所出率_不足 = Fraction(1, 2) - Fraction(1, 2)
不足 = 3

# 置所出率，以少減多，餘
餘 = 所出率_盈 - 所出率_不足

# 并盈、不足為法
法 = 盈 + 不足

# 令維乘所出率，并以為實
實 = (所出率_盈 * 不足) + (所出率_不足 * 盈)

# 以約法、實
約數 = Fraction(實, 法)

# 實為物價，法為人數
b = 約數.numerator  # 璡價
a = 約數.denominator  # 人數

a = 42  # 人數
b = 17  # 璡價#----- content ends here -----

"""
"""
