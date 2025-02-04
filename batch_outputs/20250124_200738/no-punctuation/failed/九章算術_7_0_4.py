"""
今有共買物人出八盈三人出七不足四問人數物價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 物價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying an item. One person contributes 8 and has an excess of 3. Another person contributes 7 and is short by 4.
Question: how many people are there, and what is the price of the item?

The procedure for the "Excess and Deficit" method says:
Place the contribution rates, with the excess and deficit values below them.
Multiply the contribution rates by their respective excess or deficit values, and sum them to obtain the dividend.
Sum the excess and deficit values to obtain the divisor.
Divide the dividend by the divisor to obtain 1 (the base unit). If there is a remainder, adjust it proportionally.
For those who share the purchase, place the contribution rates. Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: there are *a* people, and the price of the item is *b*.
"""

# 人出八盈三
出率1 = 8
盈1 = 3

# 人出七不足四
出率2 = 7
不足2 = 4

# 令維乘所出率并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + 不足2

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多餘以約法實
餘 = abs(出率1 - 出率2)
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 實
a = 法#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 53, Actual: 52"""
