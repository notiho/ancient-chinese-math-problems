"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a斗 
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
When the bucket is filled with millet and pounded, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficit" method to solve it. 
Suppose the original rice is 2 dou, which is 2 sheng short. 
Then suppose it is 3 dou, which is 2 sheng in excess.

The "Excess and Deficit" method says: Place the output rate, and the excess and deficit, each below their respective terms. 
Let them be multiplied by the output rate and summed to form the dividend. 
Sum the excess and deficit to form the divisor. 
Divide the dividend by the divisor. If there is a fraction, simplify it. 
If the excess and deficit are the same, place the output rate, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* dou.
"""

# 所出率
所出率 = 7  # 得米七斗

# 假令故米二斗，不足二升
假設1_故米 = 2  # 斗
假設1_不足 = Fraction(2, 10)  # 2升 = 2/10斗

# 令之三斗，有餘二升
假設2_故米 = 3  # 斗
假設2_有餘 = Fraction(2, 10)  # 2升 = 2/10斗

# 盈不足術：
# 置所出率，盈不足各居其下
盈不足1 = 假設1_不足
盈不足2 = 假設2_有餘

# 維乘所出率，并以為實
實 = (所出率 * 假設2_故米 - 所出率 * 假設1_故米)

# 并盈不足為法
法 = 盈不足1 + 盈不足2

# 實如法而一
a = Fraction(實, 法)  # 故米數 in 斗
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 35/2"""
