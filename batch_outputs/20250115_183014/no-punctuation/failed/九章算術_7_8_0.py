"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a斗 
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
The bucket is filled with millet and then pounded, resulting in 7 dou of rice.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it.
Suppose the original rice is 2 dou, which is 2 sheng short. 
Then suppose it is 3 dou, which is 2 sheng in excess.

The "Excess and Deficiency" method says: Place the output rate, and the excess and deficiency values, each below their respective assumptions.
Multiply the assumptions by the output rate, and add them together to form the dividend.
Add the excess and deficiency values together to form the divisor.
Divide the dividend by the divisor to find the result. If there is a remainder, adjust accordingly.
If the excess and deficiency are of the same type, adjust the divisor and dividend accordingly.

Answer: the original rice is *a* dou.
"""

# 所出率 (resulting rice after pounding)
所出率 = 7

# 假令故米二斗，不足二升
假設1 = 2  # 2 dou
不足1 = -Fraction(2, 10)  # 2 sheng = 2/10 dou

# 令之三斗，有餘二升
假設2 = 3  # 3 dou
盈餘2 = Fraction(2, 10)  # 2 sheng = 2/10 dou

# 盈不足術計算
# 實 = 假設1 * 盈餘2 + 假設2 * 不足1
實 = 假設1 * 盈餘2 + 假設2 * 不足1

# 法 = 盈餘2 + 不足1
法 = 盈餘2 + 不足1

# 故米數 = 實 / 法
a = Fraction(實, 法)

# Convert to dou
a = a.limit_denominator()  # Simplify fraction if necessary
"""
Code error: Fraction(-1, 0)"""
