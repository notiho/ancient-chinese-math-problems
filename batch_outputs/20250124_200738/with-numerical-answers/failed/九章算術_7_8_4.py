"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=5/2)斗 。
"""

#----- content starts here -----
"""
Suppose there is rice in a 10-dou bucket, but the amount is unknown.
When the bucket is filled with millet and pounded, 7 dou of rice is obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "excess and deficiency" method to solve it.
Suppose the original rice is 2 dou, then it is short by 2 sheng.
Suppose it is 3 dou, then there is an excess of 2 sheng.

The "excess and deficiency" method says: Place the output rates, with the excess and deficiency below each.
Multiply the assumed values by their respective output rates, and add them together to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the excess and deficiency are related to the same object being purchased, place the output rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a*(=5/2) dou.
"""

# 假令故米二斗，不足二升
假設1 = 2  # 2 dou
不足1 = Fraction(2, 10)  # 2 sheng = 2/10 dou

# 令之三斗，有餘二升
假設2 = 3  # 3 dou
盈2 = Fraction(2, 10)  # 2 sheng = 2/10 dou

# 盈不足術曰：置所出率，盈、不足各居其下
出率1 = 假設1 + 不足1  # 2 + 2/10
出率2 = 假設2 - 盈2  # 3 - 2/10

# 令維乘所出率，并以為實
實 = (假設1 * 出率2) + (假設2 * 出率1)

# 并盈、不足為法
法 = 出率1 + 出率2

# 實如法而一
a = Fraction(實, 法)  # 5/2 dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 61/25"""
