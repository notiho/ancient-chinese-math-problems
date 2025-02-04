"""
今有共買物人出八盈三人出七不足四問人數物價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 物價 b 
"""

"""
Suppose there is a group buying an item. One person contributes 8 and has an excess of 3. Another person contributes 7 and is short by 4.
Question: how many people are there, and what is the price of the item?

The procedure for the "excess and deficiency" method says:
1. Place the contribution rates, with the excess and deficiency values below them.
2. Multiply the contribution rates by their respective excess or deficiency values, and sum these to obtain the dividend (實).
3. Sum the excess and deficiency values to obtain the divisor (法).
4. Divide the dividend by the divisor to obtain the base value (實如法而一). If there is a remainder, adjust it proportionally.
5. For those who share the purchase, place the contribution rates. Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
6. The dividend gives the price of the item, and the divisor gives the number of people.

Answer: there are *a* people, and the price of the item is *b*.
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
基值 = Fraction(實, 法)

# 盈不足相與同，其買物者置所出率，以少減多餘以約法實
餘 = abs(出率1 - 出率2)
法 = 法 // 餘
實 = 實 // 餘

# 實為物價，法為人數
b = 實
a = 法
"""
Variable 'b' has wrong value. Expected: 53, Actual: 52"""
