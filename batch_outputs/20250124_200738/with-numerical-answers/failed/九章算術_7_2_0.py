"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=42)人 ，璡價 b(=17) 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a jade item. If each person contributes half a unit, there is an excess of 4 units. 
If each person contributes half a unit less, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade?

The procedure for "excess and shortfall" says:
Place the contribution rate, with the excess and shortfall below it respectively.
Multiply the contribution rate by the respective excess or shortfall, and sum them to form the dividend.
Sum the excess and shortfall to form the divisor.
Divide the dividend by the divisor to obtain 1 unit. If there are fractions, simplify them.
For those sharing the same purchased item, place the contribution rate, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend is the price of the item, and the divisor is the number of people.

Answer: *a*(=42) people, *b*(=17) is the price of the jade.
"""

# 人出半，盈四
所出率_多 = Fraction(1, 2)
盈 = 4

# 人出少半，不足三
所出率_少 = Fraction(1, 2) - Fraction(1, 2)
不足 = 3

# 令維乘所出率，并以為實
實 = (所出率_多 * 盈) + (所出率_少 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = 所出率_多 - 所出率_少
法 = 法 // 餘
實 = 實 // 餘

# 實為物價，法為人數
b = 實  # 17
a = 法  # 42#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 14
Variable 'b' has wrong value. Expected: 17, Actual: 4"""
