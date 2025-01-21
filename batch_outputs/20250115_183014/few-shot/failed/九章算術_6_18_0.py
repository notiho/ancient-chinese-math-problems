"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should each of the middle 2 nodes hold if the capacity is to be evenly distributed?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to get the lower rate, and divide the 3 sheng among the top 4 nodes to get the upper rate.
Subtract the smaller rate from the larger rate to get the difference, which is the dividend.
Place the 4 nodes and 3 nodes, halve each, and subtract from the 9 nodes to get the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the amount by which the rates decrease step by step.
The lower rate, plus 1 sheng and half a sheng less, gives the capacity of the second node from the bottom.

Answer: The capacities of the nodes are as follows:
Bottom node: *a* sheng,
Second node: *b* sheng,
Third node: *c* sheng,
Fourth node: *d* sheng,
Fifth node: *e* sheng,
Sixth node: *f* sheng,
Seventh node: *g* sheng,
Eighth node: *h* sheng,
Top node: *i* sheng.
"""

from fractions import Fraction

# 下三節容四升
下節數 = 3
下容 = 4

# 上四節容三升
上節數 = 4
上容 = 3

# 中間二節
中節數 = 2

# 以下三節分四升為下率
下率 = Fraction(下容, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上容, 上節數)

# 上下率以少減多，餘為實
實 = 下率 - 上率

# 置四節、三節，各半之
四節半 = Fraction(4, 2)
三節半 = Fraction(3, 2)

# 以減九節，餘為法
總節數 = 9
法 = 總節數 - (四節半 + 三節半)

# 實如法得一升，即衰相去也
衰相去 = Fraction(實, 法)

# 計算每節的容量
a = 下率 + 2 * 衰相去  # 下初
b = 下率 + 衰相去      # 下第二節
c = 下率               # 下第三節
d = 上率 + 衰相去      # 中第一節
e = 上率 + 衰相去      # 中第二節
f = 上率               # 上第一節
g = 上率 - 衰相去      # 上第二節
h = 上率 - 2 * 衰相去  # 上第三節
i = 上率 - 3 * 衰相去  # 上第四節
"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 17/11
Variable 'b' has wrong value. Expected: 4/3, Actual: 95/66
Variable 'c' has wrong value. Expected: 27/22, Actual: 4/3
Variable 'd' has wrong value. Expected: 37/33, Actual: 113/132
Variable 'e' has wrong value. Expected: 67/66, Actual: 113/132
Variable 'f' has wrong value. Expected: 10/11, Actual: 3/4
Variable 'g' has wrong value. Expected: 53/66, Actual: 85/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 71/132
Variable 'i' has wrong value. Expected: 13/22, Actual: 19/44"""
