"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=5/2)斗 。
"""

"""
Suppose there is rice in a 10-dou bucket, but the amount is unknown. 
When the bucket is filled with millet and pounded, it produces 7 dou of rice.
Question: how much rice was originally in the bucket?

The procedure says: Use the "Excess and Deficiency" method to solve it. 
Suppose the original rice is 2 dou, then it is short by 2 sheng. 
Suppose it is 3 dou, then there is an excess of 2 sheng.

The "Excess and Deficiency" method says: Place the rates of output, with the excess and deficiency below them respectively. 
Multiply the rates of output by their respective excess or deficiency, and sum them to obtain the dividend. 
Sum the excess and deficiency to obtain the divisor. 
Divide the dividend by the divisor to obtain the result. 
If there are fractions, simplify them. 
If the excess and deficiency are associated with the same commodity, place the rates of output, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend becomes the price of the commodity, and the divisor becomes the number of people.

Answer: *a*(=5/2) dou.
"""

# 假令故米二斗，不足二升
假設1_故米 = 2  # 2斗
不足1 = Fraction(2, 10)  # 2升 = 2/10斗

# 令之三斗，有餘二升
假設2_故米 = 3  # 3斗
有餘2 = Fraction(2, 10)  # 2升 = 2/10斗

# 盈不足術曰：置所出率，盈、不足各居其下
# 所出率 (假設的故米)
率1 = 假設1_故米
率2 = 假設2_故米

# 盈、不足
不足 = 不足1
有餘 = 有餘2

# 令維乘所出率，并以為實
實 = (率1 * 有餘) + (率2 * 不足)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # 5/2斗
"""
"""
