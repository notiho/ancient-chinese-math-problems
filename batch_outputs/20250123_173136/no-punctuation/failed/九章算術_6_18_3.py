"""
今有竹九節下三節容四升上四節容三升問中間二節欲均容各多少
術曰以下三節分四升為下率以上四節分三升為上率上下率以少減多餘為實置四節三節各半之以減九節餘為法實如法得一升即衰相去也下率一升少半升者下第二節容也
荅曰下初 a升 次 b升 次 c升 次 d升 次 e升 次 f升 次 g升 次 h升 次 i升 
"""

"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: for the middle 2 nodes, how much should each hold to make their capacities equal?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to find the bottom rate.
Divide the 3 sheng among the top 4 nodes to find the top rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract from 9 nodes. The remainder is the divisor.
Divide the dividend by the divisor to obtain 1 sheng, which is the difference between successive nodes.
For the bottom rate, subtract half a sheng to find the capacity of the second node.

Answer: the bottom-first node holds *a* sheng, the second holds *b* sheng, ..., and the ninth holds *i* sheng.
"""

from fractions import Fraction

# 下三節容四升
下三節 = 3
下容 = 4

# 上四節容三升
上四節 = 4
上容 = 3

# 中間二節
中間二節 = 2

# 以下三節分四升為下率
下率 = Fraction(下容, 下三節)

# 以上四節分三升為上率
上率 = Fraction(上容, 上四節)

# 上下率以少減多餘為實
實 = abs(上率 - 下率)

# 置四節三節各半之以減九節餘為法
法 = 9 - (下三節 + 上四節) / 2

# 實如法得一升即衰相去也
衰相去 = Fraction(實, 法)

# 計算每節的容量
a = 下率 - 2 * 衰相去
b = 下率 - 衰相去
c = 下率
d = 下率 + 衰相去
e = 下率 + 2 * 衰相去
f = 上率 + 2 * 衰相去
g = 上率 + 衰相去
h = 上率
i = 上率 - 衰相去
"""
Code error: both arguments should be Rational instances"""
