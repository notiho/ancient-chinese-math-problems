"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=42)人 ，璡價 b(=17) 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a jade object. 
If each person contributes half a unit, there is an excess of 4 units.
If each person contributes half a unit less, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade object?

The procedure for excess and shortfall says: Place the contribution rates, with the excess and shortfall below them.
Multiply the contribution rates by their respective multipliers, and add them together to form the dividend.
Add the excess and shortfall to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For cases where the excess and shortfall relate to the same purchased object, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend gives the price of the object, and the divisor gives the number of people.

Answer: *a*(=42) people, and the price of the jade object is *b*(=17).
"""

# 人出半，盈四
所出率_多 = Fraction(1, 2)
盈 = 4

# 人出少半，不足三
所出率_少 = Fraction(1, 2) - Fraction(1, 2)
不足 = 3

# 置所出率，以少減多，餘
所出率差 = 所出率_多 - 所出率_少

# 盈、不足相加為法
法 = 盈 + 不足

# 令維乘所出率，并以為實
實 = (所出率_多 * 不足) + (所出率_少 * 盈)

# 以約法、實
人數 = Fraction(實, 法)
璡價 = Fraction#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
