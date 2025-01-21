"""
今有共買璡人出半盈四人出少半不足三問人數璡價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 璡價 b 
"""

"""
Suppose there is a group of people buying a jade object together. 
Some people contribute half, and there is a surplus of 4. 
Other people contribute less than half, and there is a shortfall of 3. 
Question: how many people are there, and what is the price of the jade object?

The procedure for surplus and shortfall says: 
Place the rates of contribution, with surplus and shortfall each below their respective rates. 
Multiply the rates of contribution, and sum them to form the dividend. 
Sum the surplus and shortfall to form the divisor. 
Divide the dividend by the divisor. If there is a fraction, resolve it. 
The surplus and shortfall are treated equally. 
For those buying the object, place the rates of contribution, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* people, jade price *b*.
"""

# 盈四
盈 = 4

# 不足三
不足 = 3

# 出半
出半率 = Fraction(1, 2)

# 出少半
出少半率 = Fraction(1, 2) - Fraction(1, 2)

# 置所出率，盈不足各居其下
所出率_盈 = 出半率
所出率_不足 = 出少半率

# 令維乘所出率，并以為實
實 = (所出率_盈 * 不足) + (所出率_不足 * 盈)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
人數 = Fraction(實, 法)

# 有分者通之，盈不足相與同
人數 = 人數.limit_denominator()

# 其買物者置所出率，以少減多，餘以約法實
餘 = abs(所出率_盈 - 所出率_不足)
法 = 法 * 餘
實 = 實 * 餘

# 實為物價，法為人數
b = 實
a = 法
"""
Variable 'a' has wrong value. Expected: 42, Actual: 7/2
Variable 'b' has wrong value. Expected: 17, Actual: 3/4"""
