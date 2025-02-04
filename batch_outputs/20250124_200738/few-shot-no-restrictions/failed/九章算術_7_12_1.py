"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) worth 50 qian per dou, and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, one can obtain 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving an excess of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.

The method of surplus and deficit (盈不足術) says: Place the rates of output, with surplus and deficit below each.
Multiply the rates of output by their respective surplus or deficit, and sum them to obtain the dividend (實).
Sum the surplus and deficit to obtain the divisor (法).
Divide the dividend by the divisor to obtain the result.
If there is a remainder, simplify it.
For surplus and deficit problems involving goods, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: *a* sheng of pure wine, and *b* dou of diluted wine.
"""

from fractions import Fraction

# Prices and total money
醇酒價 = 50  # qian per dou
行酒價 = 10  # qian per dou
總錢 = 30  # qian
總酒 = 2  # dou

# Surplus and deficit setup
# First assumption: 5 sheng of pure wine, 1 dou 5 sheng of diluted wine
盈 = 10  # surplus of 10 qian
醇酒率1 = Fraction(5, 10)  # 5 sheng = 0.5 dou
行酒率1 = Fraction(15, 10)  # 1 dou 5 sheng = 1.5 dou

# Second assumption: 2 sheng of pure wine, 1 dou 8 sheng of diluted wine
不足 = 2  # deficit of 2 qian
醇酒率2 = Fraction(2, 10)  # 2 sheng = 0.2 dou
行酒率2 = Fraction(18, 10)  # 1 dou 8 sheng = 1.8 dou

# 盈不足術 calculations
# Multiply rates by surplus/deficit and sum them
實 = (醇酒率1 * 盈 + 行酒率1 * 盈) + (醇酒率2 * 不足 + 行酒率2 * 不足)

# Sum surplus and deficit
法 = 盈 + 不足

# Divide 实 by 法 to find the amount of pure wine
醇酒量 = Fraction(實, 法)

# Calculate the amount of 行酒
行酒量 = 總酒 - 醇酒量

# Convert to sheng and dou
a = 醇酒量 * 10  # Convert to sheng
b = 行酒量  # Already in dou

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 20
Variable 'b' has wrong value. Expected: 7/4, Actual: 0"""
