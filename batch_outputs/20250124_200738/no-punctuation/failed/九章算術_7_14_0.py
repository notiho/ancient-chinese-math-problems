"""
今有漆三得油四油四和漆五今有漆三斗欲令分以易油還自和餘漆問出漆得油和漆各幾何
術曰假令出漆九升不足六升令之出漆一斗二升有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰出漆 a斗 得油 b斗 和漆 c斗  d升 
"""

#----- content starts here -----
"""
Suppose there are 3 dou of lacquer that yield 4 dou of oil. 
4 dou of oil mixed with 5 dou of lacquer creates a mixture.
Now, given 3 dou of lacquer, it is desired to exchange it for oil, and then mix the remaining lacquer with the oil.
Question: how much lacquer is exchanged, how much oil is obtained, and how much of the mixture is created?

The procedure says: Suppose 9 sheng of lacquer is exchanged, but it is insufficient by 6 sheng. 
Adjust it to exchange 1 dou and 2 sheng, leaving 2 sheng remaining.

The procedure for surplus and deficit says: Place the rate of exchange, the surplus, and the deficit below it.
Let them be multiplied by the rate of exchange and summed to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, simplify it.
The surplus and deficit are treated equally.
For the exchanged material, place the rate of exchange, subtract the smaller from the larger, and reduce the divisor and dividend.
The dividend is the value of the material, and the divisor is the number of people.

Answer: Exchanged lacquer is *a* dou, obtained oil is *b* dou, and the mixture is *c* dou and *d* sheng.
"""

from fractions import Fraction

# 漆三得油四 (3 dou of lacquer yields 4 dou of oil)
漆率 = 3
油率 = 4

# 油四和漆五 (4 dou of oil mixed with 5 dou of lacquer creates a mixture)
油和率 = 4
漆和率 = 5

# 今有漆三斗 (Given 3 dou of lacquer)
漆總量 = 3

# Step 1: Calculate the lacquer exchanged for oil
# 漆三得油四 -> 漆率 : 油率 = 3 : 4
# To find the lacquer exchanged, we use the same ratio
出漆 = 漆總量  # Assume all lacquer is exchanged for oil
得油 = Fraction(出漆 * 油率, 漆率)

# Step 2: Calculate the remaining lacquer after exchange
餘漆 = 漆總量 - 出漆

# Step 3: Calculate the mixture created
# 油四和漆五 -> 油和率 : 漆和率 = 4 : 5
# To find the total mixture, use the same ratio
和漆 = 餘漆
和油 = Fraction(和漆 * 油和率, 漆和率)
混合物 = 和漆 + 和油

# Convert results to dou and sheng (1 dou = 10 sheng)
a = 出漆  # Exchanged lacquer in dou
b = 得油  # Obtained oil in dou
c = int(混合物)  # Whole dou of mixture
d = int((混合物 - c) * 10)  # Remaining sheng of mixture

a, b, c, d#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
