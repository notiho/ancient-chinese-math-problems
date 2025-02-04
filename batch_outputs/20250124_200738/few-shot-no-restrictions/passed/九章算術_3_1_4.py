"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are cows, horses, and sheep eating a farmer's crops. The farmer demands compensation of 5 dou of millet.
The sheep owner says, "My sheep ate half as much as a horse."
The horse owner says, "My horse ate half as much as a cow."
Now, to fairly divide the compensation, how much should each owner pay?

The procedure says: Assign weights to the cow as 4, the horse as 2, and the sheep as 1. 
Each is treated as a separate term in a decreasing sequence.
Add these weights together to form the divisor.
Multiply the 5 dou of millet by the weights of each term (before summing them) to form the dividend.
Divide the dividend by the divisor to find the contribution of each.

Answer: The cow owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

from fractions import Fraction

# Compensation demanded
粟 = 5  # in dou

# Assign weights
牛 = 4
馬 = 2
羊 = 1

# Calculate the divisor (sum of weights)
法 = 牛 + 馬 + 羊

# Calculate the contributions (dividends)
牛實 = 粟 * 牛
馬實 = 粟 * 馬
羊實 = 粟 * 羊

# Divide each by the divisor to find the contributions
a = Fraction(牛實, 法)  # 牛主出 a斗
b = Fraction(馬實, 法)  # 馬主出 b斗
c = Fraction(羊實, 法) * 10  # 羊主出 c升 (1 dou = 10 sheng)

# Output the results
a, b, c#----- content ends here -----

"""
"""
