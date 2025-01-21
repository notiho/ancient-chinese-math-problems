"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=5/2)斗 。
"""

"""
Suppose there is rice in a 10-dou bucket, but the amount is unknown. 
When the bucket is filled with millet and pounded, it produces 7 dou of rice.
Question: how much rice was originally in the bucket?

The procedure says: Use the "surplus and deficit" method to solve it.
Suppose the original rice is 2 dou, then it is short by 2 sheng.
Suppose it is 3 dou, then there is an excess of 2 sheng.

The "surplus and deficit" method says: Place the rates of output, with the surplus and deficit below each.
Multiply the rates of output by their respective surplus or deficit, and add them together to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
If the surplus and deficit correspond to the same item being purchased, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the value of the item, and the divisor becomes the number of people.

Answer: *a*(=5/2) dou.
"""

# 假令故米二斗，不足二升
假米1 = 2  # 2 dou
不足1 = Fraction(2, 10)  # 2 sheng = 2/10 dou

# 令之三斗，有餘二升
假米2 = 3  # 3 dou
盈2 = Fraction(2, 10)  # 2 sheng = 2/10 dou

# 盈不足術曰：置所出率，盈、不足各居其下
所出率1 = 假米1
所出率2 = 假米2

# 令維乘所出率，并以為實
實 = (所出率1 * 盈2) + (所出率2 * 不足1)

# 并盈、不足為法
法 = 盈2 + 不足1

# 實如法而一
a = Fraction(實, 法)  # 5/2 dou
"""
"""
