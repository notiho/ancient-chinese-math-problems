"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are cattle, horses, and sheep that ate someone's crops. The crop owner demands 5 dou of millet as compensation.
The sheep owner says: "My sheep ate half as much as a horse."
The horse owner says: "My horse ate half as much as a cow."
Now, to divide the compensation proportionally, how much should each pay?

The procedure says: Assign weights to the cow, horse, and sheep as 4, 2, and 1 respectively, each forming a decreasing sequence.
Add these weights together to form the divisor.
Multiply the 5 dou of millet by the weights of each animal to form the dividends.
Divide each dividend by the divisor to calculate the amount of millet owed by each.

The answer says: the cow owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

from fractions import Fraction

# Assign weights to the animals
牛 = 4
馬 = 2
羊 = 1

# Calculate the divisor (sum of weights)
法 = 牛 + 馬 + 羊

# Total compensation in dou
總粟 = 5

# Calculate the millet owed by each owner
牛實 = 牛 * 總粟
馬實 = 馬 * 總粟
羊實 = 羊 * 總粟

# Divide by the divisor to get the amount each owes
牛出 = Fraction(牛實, 法)  # in dou
馬出 = Fraction(馬實, 法)  # in dou
羊出 = Fraction(羊實, 法)  # in dou

# Convert the sheep's payment to sheng (1 dou = 10 sheng)
羊出升 = 羊出 * 10

# Final results
a = 牛出
b = 馬出
c = 羊出升

# Output
a, b, c  # 牛主出 a斗, 馬主出 b斗, 羊主出 c升#----- content ends here -----

"""
"""
