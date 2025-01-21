"""
今有共買璡人出半盈四人出少半不足三問人數璡價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 璡價 b 
"""

"""
Suppose there is a group of people buying jade together. 
One person contributes half, which is surplus by 4. 
Four people contribute less than half, which is short by 3. 
Question: how many people are there, and what is the price of the jade?

The procedure for surplus and shortfall says: 
Place the contribution rates, with surplus and shortfall each below their respective rates. 
Multiply the contribution rates, sum them, and take this as the dividend. 
Sum the surplus and shortfall, and take this as the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there are fractions, simplify them. 
The surplus and shortfall are treated equally. 
For those buying the item, place the contribution rates. 
Subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* people, and the price of the jade is *b*.
"""

# 盈不足術
# 置所出率
所出率_盈 = Fraction(1, 2)  # 一人出半
所出率_不足 = Fraction(1, 2)  # 四人出少半

# 盈不足各居其下
盈 = 4  # 盈四
不足 = 3  # 不足三

# 令維乘所出率并以為實
實 = (所出率_盈 * 不足) + (所出率_不足 * 盈)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
人數 = Fraction(實, 法)

# 有分者通之
人數 = 人數.limit_denominator()

# 盈不足相與同其買物者
# 置所出率，以少減多餘以約法實
餘 = abs(所出率_盈 - 所出率_不足)
法 = 法 * 餘
實 = 實 * 餘

# 實為物價，法為人數
b = 實
a = 法

a = a.limit_denominator()
b = b.limit_denominator()
"""
Variable 'a' has wrong value. Expected: 42, Actual: 0
Variable 'b' has wrong value. Expected: 17, Actual: 0"""
