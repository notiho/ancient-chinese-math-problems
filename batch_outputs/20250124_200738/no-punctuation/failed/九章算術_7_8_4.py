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

The procedure says: Use the "Excess and Deficiency" method to solve this.
Suppose the original rice is 2 dou, which is 2 sheng short.
Suppose it is 3 dou, which is 2 sheng in excess.

The "Excess and Deficiency" method says: Place the output rates, and place the excess and deficiency below them.
Multiply the output rates, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor, and if there is a remainder, adjust accordingly.
If the excess and deficiency are of the same sign, adjust the divisor and dividend accordingly.

Answer: *a* dou of rice.
"""

# Known values
桶容量 = 10  # 10斗桶
所得米 = 7  # 舂後得米7斗

# 假令故米2斗，不足2升
假設1_米 = 2  # 假設1的米數
不足1 = -Fraction(2, 10)  # 不足2升，轉為斗 (1斗 = 10升)

# 假令故米3斗，有餘2升
假設2_米 = 3  # 假設2的米數
有餘2 = Fraction(2, 10)  # 有餘2升，轉為斗

# 盈不足術計算
# 置所出率
所出率1 = 所得米 - 假設1_米  # 假設1的出率
所出率2 = 所得米 - 假設2_米  # 假設2的出率

# 維乘所出率，并以為實
實 = (所出率1 * 有餘2) - (所出率2 * 不足1)

# 并盈不足為法
法 = 有餘2 - 不足1

# 實如法而一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 9/2"""
