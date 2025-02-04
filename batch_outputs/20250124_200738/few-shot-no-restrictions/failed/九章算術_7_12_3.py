"""
今有醇酒一斗，直錢五十；行酒一斗，直錢一十。今將錢三十，得酒二斗。問︰醇、行酒各得幾何？
術曰：假令醇酒五升，行酒一斗五升，有餘一十。令之醇酒二升，行酒一斗八升，不足二。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：醇酒 a升 ，行酒 b斗 。
"""

#----- content starts here -----
"""
Suppose there is pure wine (醇酒) worth 50 qian per dou and diluted wine (行酒) worth 10 qian per dou.
Now, with 30 qian, you can buy 2 dou of wine in total.
Question: how much pure wine and diluted wine are obtained respectively?

The procedure says: Suppose there are 5 sheng of pure wine and 1 dou 5 sheng of diluted wine, leaving a surplus of 10 qian.
Suppose there are 2 sheng of pure wine and 1 dou 8 sheng of diluted wine, falling short by 2 qian.

The method of surplus and deficit (盈不足術) says: Place the price rates of the items, and place the surplus and deficit below them.
Cross-multiply the price rates with the surplus and deficit, and sum them to form the dividend (實).
Sum the surplus and deficit to form the divisor (法).
Divide the dividend by the divisor to find the result.
If there is a remainder, adjust accordingly.
The surplus and deficit are then used to determine the quantities of the items.

Answer: *a* sheng of pure wine and *b* dou of diluted wine.
"""

from fractions import Fraction

# Prices of pure wine and diluted wine
醇酒價 = 50  # qian per dou
行酒價 = 10  # qian per dou

# Total money and total wine
總錢 = 30  # qian
總酒 = 2  # dou

# Surplus and deficit scenarios
盈 = 10  # surplus in qian
不足 = 2  # deficit in qian

# Cross-multiply the price rates with surplus and deficit
實 = (行酒價 * 盈) + (醇酒價 * 不足)

# Sum the surplus and deficit to form the divisor
法 = 盈 + 不足

# Divide to find the amount of pure wine in dou
醇酒量 = Fraction(實, 法)

# Calculate the amount of diluted wine in dou
行酒量 = 總酒 - 醇酒量

# Convert to sheng (1 dou = 10 sheng)
a = 醇酒量 * 10  # pure wine in sheng
b = 行酒量  # diluted wine in dou

# Output the results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 500/3
Variable 'b' has wrong value. Expected: 7/4, Actual: -44/3"""
