"""
今有竹九節，下三節容四升，上四節容三升。問︰中間二節欲均容各多少？
術曰：以下三節分四升為下率，以上四節分三升為上率。上下率以少減多，餘為實。置四節、三節，各半之，以減九節，餘為法。實如法得一升，即衰相去也。下率，一升、少半升者，下第二節容也。
荅曰：下初， a升 ，次 b升 ，次 c升 ，次 d升 ，次 e升 ，次 f升 ，次 g升 ，次 h升 ，次 i升 。
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: how much should the middle 2 nodes hold to make the distribution even?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to get the lower rate, and divide the 3 sheng among the top 4 nodes to get the upper rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, halve each of them, and subtract from the 9 nodes. The remainder is the divisor.
Divide the dividend by the divisor to get 1 sheng, which is the difference between successive nodes.
The lower rate plus 1 sheng and half of 1 sheng is the amount held by the second node from the bottom.

Answer: The bottom node holds *a* sheng, the second holds *b* sheng, ..., and the top node holds *i* sheng.
"""

from fractions import Fraction

# 下三節容四升
下節數 = 3
下容積 = 4

# 上四節容三升
上節數 = 4
上容積 = 3

# 以下三節分四升為下率
下率 = Fraction(下容積, 下節數)

# 以上四節分三升為上率
上率 = Fraction(上容積, 上節數)

# 上下率以少減多，餘為實
實 = 下率 - 上率

# 置四節、三節，各半之，以減九節，餘為法
法 = 9 - (Fraction(下節數, 2) + Fraction(上節數, 2))

# 實如法得一升，即衰相去也
衰相去 = Fraction(實, 法)

# 計算每節的容積
節容積 = []
for i in range(9):
    if i == 0:  # 第一節
        節容積.append(下率)
    else:
        節容積.append(節容積[i - 1] + 衰相去)

# 將結果分配到各節
a, b, c, d, e, f, g, h, i = 節容積#----- content ends here -----

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
