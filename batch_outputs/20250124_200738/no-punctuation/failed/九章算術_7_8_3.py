"""
今有米在十斗桶中不知其數滿中添粟而舂之得米七斗問故米幾何
術曰以盈不足術求之假令故米二斗不足二升令之三斗有餘二升
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a斗 
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
The bucket is filled with millet, and after pounding, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it.
Suppose the original rice is 2 dou, which is 2 sheng short.
Then suppose it is 3 dou, which is 2 sheng in excess.

The "Excess and Deficiency" method says: Place the output rate, and the excess and deficiency values below it.
Multiply the output rate by the excess and deficiency values, and add them together to form the dividend.
Add the excess and deficiency values together to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the excess and deficiency are of the same type, adjust accordingly.

Answer: *a* dou.
"""

# 所出率 (舂後得米)
所出率 = 7

# 假令故米二斗，不足二升
假設1_斗 = 2
不足1_升 = Fraction(2, 10)  # 2升 = 2/10斗

# 假令故米三斗，有餘二升
假設2_斗 = 3
有餘2_升 = Fraction(2, 10)  # 2升 = 2/10斗

# 盈不足術計算
# 置所出率，盈不足各居其下
盈不足1 = 所出率 - 假設1_斗 - 不足1_升
盈不足2 = 假設2_斗 + 有餘2_升 - 所出率

# 維乘所出率，并以為實
實 = (盈不足1 * 假設2_斗) + (盈不足2 * 假設1_斗)

# 并盈不足為法
法 = 盈不足1 + 盈不足2

# 實如法而一
a = Fraction(實, 法)  # 結果為原來的米數 (斗)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 34/5"""
