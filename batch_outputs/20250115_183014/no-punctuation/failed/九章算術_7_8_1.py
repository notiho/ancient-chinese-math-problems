"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a斗 
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
When the bucket is filled with millet and then pounded, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it. 
Suppose the original rice was 2 dou, but it is 2 sheng short. 
Suppose it was 3 dou, but it exceeds by 2 sheng.

The "Excess and Deficiency" method says: Place the output rate, and the excess and deficiency, each below their respective assumptions.
Multiply the output rate by the assumptions and combine them to form the dividend.
Combine the excess and deficiency to form the divisor.
Divide the dividend by the divisor. If there is a remainder, adjust it.
If the excess and deficiency are the same, place the output rate, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the value of the goods, and the divisor becomes the number of people.

Answer: *a* dou.
"""

# 所出率
所出率 = 7  # 得米七斗

# 假令故米二斗不足二升
假設1 = 2  # 斗
不足1 = -Fraction(2, 10)  # 2升 = 2/10斗

# 假令故米三斗有餘二升
假設2 = 3  # 斗
盈餘2 = Fraction(2, 10)  # 2升 = 2/10斗

# 盈不足術
# 置所出率，盈不足各居其下
實1 = 所出率 * 假設1 + 不足1
實2 = 所出率 * 假設2 + 盈餘2

# 并盈不足為法
法 = 假設2 - 假設1

# 實如法而一
實 = 實2 - 实1

# 有分者通之
a = Fraction(實, 法) + 假設1
"""
Code error: name '实1' is not defined"""
