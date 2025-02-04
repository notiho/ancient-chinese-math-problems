"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

"""
Suppose there is a bamboo with nine nodes. The bottom three nodes hold 4 sheng, and the top four nodes hold 3 sheng.
Question: how much should the middle two nodes hold to balance the capacity equally?

The procedure says: Divide the 4 sheng among the bottom three nodes to get the lower rate, and divide the 3 sheng among the top four nodes to get the upper rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the four nodes and three nodes, halve each, and subtract from the nine nodes. The remainder is the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the difference between successive nodes.
The lower rate plus 1 sheng and half of 1 sheng is the capacity of the second node from the bottom.

Answer: For the bottom node, *a* sheng; for the second node, *b* sheng; for the third node, *c* sheng; for the fourth node, *d* sheng; for the fifth node, *e* sheng; for the sixth node, *f* sheng; for the seventh node, *g* sheng; for the eighth node, *h* sheng; for the ninth node, *i* sheng.
"""

# 下三節容四升
下三節 = 3
下容 = 4

# 上四節容三升
上四節 = 4
上容 = 3

# 以下三節分四升為下率
下率 = Fraction(下容, 下三節)

# 以上四節分三升為上率
上率 = Fraction(上容, 上四節)

# 上下率以少減多，餘為實
實 = 下率 - 上率

# 置四節、三節，各半之
四節半 = Fraction(4, 2)
三節半 = Fraction(3, 2)

# 以減九節，餘為法
九節 = 9
法 = 九節 - (四節半 + 三節半)

# 實如法得一升，即衰相去也
一升 = Fraction(實, 法)

# 計算每節的容量
a = 下率  # 第一節
b = 下率 + 一升  # 第二節
c = 下率 + 2 * 一升  # 第三節
d = 下率 + 3 * 一升  # 第四節
e = 下率 + 4 * 一升  # 第五節
f = 下率 + 5 * 一升  # 第六節
g = 下率 + 6 * 一升  # 第七節
h = 下率 + 7 * 一升  # 第八節
i = 下率 + 8 * 一升  # 第九節
"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 4/3
Variable 'b' has wrong value. Expected: 4/3, Actual: 95/66
Variable 'c' has wrong value. Expected: 27/22, Actual: 17/11
Variable 'd' has wrong value. Expected: 37/33, Actual: 109/66
Variable 'e' has wrong value. Expected: 67/66, Actual: 58/33
Variable 'f' has wrong value. Expected: 10/11, Actual: 41/22
Variable 'g' has wrong value. Expected: 53/66, Actual: 65/33
Variable 'h' has wrong value. Expected: 23/33, Actual: 137/66
Variable 'i' has wrong value. Expected: 13/22, Actual: 24/11"""
