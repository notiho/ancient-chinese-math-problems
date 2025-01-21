"""
今有共買璡人出半盈四人出少半不足三問人數璡價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 璡價 b 
"""

"""
Suppose there is a group of people buying a jade object together. 
One person contributes half, which is surplus by 4. 
Four people contribute less than half, which is short by 3. 
Question: how many people are there, and what is the price of the jade object?

The procedure for surplus and shortfall says: 
Place the rates of contribution, with surplus and shortfall each below their respective rates. 
Multiply the rates of contribution, and sum them to form the dividend. 
Sum the surplus and shortfall to form the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there is a fraction, simplify it. 
The surplus and shortfall are treated equally. 
For those buying the object, place the rates of contribution. 
Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* people, jade price *b*.
"""

# 盈不足術
# 一人出半盈四
盈率 = Fraction(1, 2)
盈 = 4

# 四人出少半不足三
不足率 = Fraction(1, 2)
不足 = 3

# 置所出率，盈不足各居其下
# 令維乘所出率，并以為實
實 = 盈率 * 不足 + 不足率 * 盈

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
結果 = Fraction(實, 法)

# 有分者通之，盈不足相與同
# 其買物者置所出率，以少減多
餘 = abs(盈率 - 不足率)

# 餘以約法實
法 = 法 / 餘
實 = 實 / 餘

# 實為物價，法為人數
a = 法  # 人數
b = 實  # 璡價
"""
Code error: Fraction(1, 0)"""
