"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a斗 
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
The bucket is filled with millet, and after pounding, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it.
Suppose the original rice was 2 dou but is short by 2 sheng. 
Then suppose it was 3 dou but exceeds by 2 sheng.

The "Excess and Deficiency" method says: 
Place the rates of output and the excess and deficiency values below them, respectively.
Multiply the rates of output by their respective excess or deficiency values, and sum them to obtain the dividend.
Sum the absolute values of the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
If the excess and deficiency are of the same type (both excess or both deficiency), adjust accordingly.

Answer: the original rice is *a* dou.
"""

# 所出率
率1 = 2  # 假令故米二斗
率2 = 3  # 假令故米三斗

# 盈不足
不足1 = -Fraction(2, 10)  # 不足二升 (2升 = 2/10斗)
盈2 = Fraction(2, 10)     # 有餘二升 (2升 = 2/10斗)

# 實：維乘所出率并以為實
實 = (率1 * 盈2) + (率2 * 不足1)

# 法：并盈不足為法
法 = abs(盈2) + abs(不足1)

# 實如法而一
a = Fraction(實, 法)  # 原來的米數 in 斗
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: -1/2"""
