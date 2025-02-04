"""
今有共買物人出八盈三人出七不足四問人數物價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 物價 b 
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy an item. One person contributes 8 and has an excess of 3. Another person contributes 7 and is short by 4.
Question: how many people are there, and what is the price of the item?

The procedure for the "excess and deficiency" method says:
1. Place the contribution rates, with the excess and deficiency values below them.
2. Multiply the contribution rates by their respective excess or deficiency values, summing them to obtain the dividend.
3. Sum the excess and deficiency values to obtain the divisor.
4. Divide the dividend by the divisor to obtain 1 unit. If there is a fraction, make it uniform.
5. If the excess and deficiency are the same, those who jointly buy the item are determined.
6. Place the contribution rates, subtract the smaller from the larger, and reduce the divisor and dividend by their greatest common divisor.
7. The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# 人出八盈三
出率1 = 8
盈1 = 3

# 人出七不足四
出率2 = 7
不足2 = -4

# 置所出率盈不足各居其下，令維乘所出率并以為實
實 = (出率1 * 盈1) + (出率2 * 不足2)

# 并盈不足為法
法 = 盈1 + abs(不足2)

# 實如法而一
單位值 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率以少減多餘以約法實
差 = abs(出率1 - 出率2)

# 以少減多餘，以約法實
物價 = 差 * 單位值
人數 = Fraction(實, 差)

# 答案
a = int(人數)
b = int(物價)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: -4
Variable 'b' has wrong value. Expected: 53, Actual: 0"""
