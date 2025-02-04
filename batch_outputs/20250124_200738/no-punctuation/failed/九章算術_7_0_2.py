"""
今有共買物人出八盈三人出七不足四問人數物價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 物價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying an item. One person contributes 8 and has an excess of 3. Another person contributes 7 and is short by 4.
Question: how many people are there, and what is the price of the item?

The procedure for the "excess and deficit" method says:
1. Place the contribution rates, with the excess and deficit amounts below each.
2. Multiply the contribution rates by their respective excess or deficit amounts, and sum these to form the dividend (實).
3. Add the excess and deficit amounts to form the divisor (法).
4. Divide the dividend by the divisor to find the unit price of the item. If there is a remainder, adjust it to ensure consistency.
5. To find the number of people, subtract the smaller contribution rate from the larger one, and use this difference to simplify the divisor and dividend.
6. The simplified dividend gives the price of the item, and the simplified divisor gives the number of people.

Answer: *a* people, and the price of the item is *b*.
"""

# 人出八盈三
出率1 = 8
盈1 = 3

# 人出七不足四
出率2 = 7
不足2 = 4

# 置所出率，盈不足各居其下
# 令維乘所出率，并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一
物價 = Fraction(實, 法)

# 盈不足相與同，其買物者置所出率，以少減多
差 = 出率1 - 出率2

# 餘以約法實
簡化法 = 法 / abs(差)
簡化實 = 實 / abs(差)

# 實為物價，法為人數
b = Fraction(簡化實, 簡化法)
a = abs(簡化法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
