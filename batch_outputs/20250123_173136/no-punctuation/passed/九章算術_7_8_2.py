"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a斗 
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
The bucket is filled with millet, and after pounding, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it.
Suppose the original rice is 2 dou, which is 2 sheng short. 
Then suppose it is 3 dou, which is 2 sheng in excess.

The "Excess and Deficiency" method says: Place the output rates (results) under the respective excess and deficiency values. 
Multiply the output rates by their respective excess or deficiency values, and sum these to form the dividend (實). 
Sum the excess and deficiency values to form the divisor (法). 
Divide the dividend by the divisor to find the result. 
If there is a remainder, convert it into the appropriate fraction. 
If the excess and deficiency are of the same type (both excess or both deficiency), subtract the smaller from the larger, and simplify the divisor and dividend accordingly. 
The result is the price of the item, and the divisor is the number of people.

Answer: *a* dou.
"""

# 假令故米二斗不足二升
假1_米 = 2  # 斗
假1_不足 = -Fraction(2, 10)  # 2升 = 2/10斗

# 令之三斗有餘二升
假2_米 = 3  # 斗
假2_有餘 = Fraction(2, 10)  # 2升 = 2/10斗

# 置所出率盈不足各居其下
所出率1 = 假1_米 + 假1_不足
所出率2 = 假2_米 + 假2_有餘

# 維乘所出率并以為實
實 = (所出率1 * 假2_有餘) + (所出率2 * abs(假1_不足))

# 并盈不足為法
法 = abs(假1_不足) + 假2_有餘

# 實如法而一
a = Fraction(實, 法)
"""
"""
