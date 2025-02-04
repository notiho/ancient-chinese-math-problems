"""
今有共買璡人出半盈四人出少半不足三問人數璡價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a人 璡價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying jade together. 
One person contributes half, which is surplus by 4. 
Four people contribute less than half, which is short by 3. 
Question: how many people are there, and what is the price of the jade?

The procedure for surplus and shortfall says: 
Place the contribution rates, with the surplus and shortfall below them respectively. 
Multiply the contribution rates and add them together to form the dividend. 
Add the surplus and shortfall to form the divisor. 
Divide the dividend by the divisor to obtain 1. 
If there is a fraction, simplify it. 
The surplus and shortfall are treated equally. 
For the buyers, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: there are *a* people, and the price of the jade is *b*.
"""

from fractions import Fraction

# One person contributes half, surplus by 4
多出率 = Fraction(1, 2)
盈 = 4

# Four people contribute less than half, shortfall by 3
少出率 = Fraction(1, 2)
不足 = 3
人數_少 = 4

# Multiply contribution rates and add them together to form the dividend
實 = (多出率 * 1) + (少出率 * 人數_少)

# Add surplus and shortfall to form the divisor
法 = 盈 + 不足

# Divide the dividend by the divisor to obtain 1
物價 = Fraction(實, 法)

# For the buyers, subtract the smaller rate from the larger rate
餘 = 多出率 - 少出率

# Simplify the divisor and dividend using the remainder
法 = 法 * 餘
實 = 實 * 餘

# The dividend becomes the price of the jade
b = 實

# The divisor becomes the number of people
a = 法#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 0
Variable 'b' has wrong value. Expected: 17, Actual: 0"""
