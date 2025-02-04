"""
今有竹九節下三節容四升上四節容三升問中間二節欲均容各多少
術曰以下三節分四升為下率以上四節分三升為上率上下率以少減多餘為實置四節三節各半之以減九節餘為法實如法得一升即衰相去也下率一升少半升者下第二節容也
荅曰下初 a升 次 b升 次 c升 次 d升 次 e升 次 f升 次 g升 次 h升 次 i升 
"""

#----- content starts here -----
"""
Suppose there is a bamboo with 9 nodes. The bottom 3 nodes hold 4 sheng, and the top 4 nodes hold 3 sheng.
Question: for the middle 2 nodes, how much should each hold to balance the distribution?

The procedure says: Divide the 4 sheng among the bottom 3 nodes to find the lower rate.
Divide the 3 sheng among the top 4 nodes to find the upper rate.
Subtract the smaller rate from the larger rate, and the remainder is the dividend.
Place the 4 nodes and 3 nodes, each halved, and subtract them from the 9 nodes. The remainder is the divisor.
Divide the dividend by the divisor to find 1 sheng, which is the difference in rates.
The lower rate plus half the difference is the amount for the second node from the bottom.

Answer: The first node holds *a* sheng, the second *b* sheng, the third *c* sheng, the fourth *d* sheng, the fifth *e* sheng, the sixth *f* sheng, the seventh *g* sheng, the eighth *h* sheng, and the ninth *i* sheng.
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

# 上下率以少減多餘為實
實 = abs(下率 - 上率)

# 置四節三節各半之
四節半 = Fraction(4, 2)
三節半 = Fraction(3, 2)

# 以減九節餘為法
九節 = 9
法 = 九節 - (四節半 + 三節半)

# 實如法得一升
一升 = Fraction(實, 法)

# 下初節
a = 下率 - 一升
# 下第二節
b = 下率 + Fraction(一升, 2)
# 下第三節
c = 下率 + 一升

# 中間二節均容
d = 下率 + 一升 + Fraction(一升, 2)
e = 下率 + 一升 + Fraction(一升, 2)

# 上初節
f = 上率 + 一升
# 上第二節
g = 上率 + Fraction(一升, 2)
# 上第三節
h = 上率
# 上第四節
i = 上率 - 一升#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 95/66, Actual: 27/22
Variable 'b' has wrong value. Expected: 4/3, Actual: 61/44
Variable 'c' has wrong value. Expected: 27/22, Actual: 95/66
Variable 'd' has wrong value. Expected: 37/33, Actual: 197/132
Variable 'e' has wrong value. Expected: 67/66, Actual: 197/132
Variable 'f' has wrong value. Expected: 10/11, Actual: 113/132
Variable 'h' has wrong value. Expected: 23/33, Actual: 3/4
Variable 'i' has wrong value. Expected: 13/22, Actual: 85/132"""
