"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=5/2)斗 。
"""

"""
Suppose there is rice in a 10-dou bucket, but the amount is unknown. When the bucket is filled with millet and pounded, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Using the "excess and deficiency" method, assume the original rice is 2 dou, but it is short by 2 sheng. Assume it is 3 dou, but there is an excess of 2 sheng.

The "excess and deficiency" method says: Place the rates of output, with the excess and deficiency below them respectively.
Multiply the assumed values by their respective rates of output, and combine them to form the dividend.
Combine the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
If the excess and deficiency relate to the same item being purchased, place the rates of output, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a*(=5/2) dou.
"""

# 假令故米二斗，不足二升
假1 = 2  # 假設的米數 (斗)
不足1 = -Fraction(2, 10)  # 不足 2 升，轉換為斗 (1斗 = 10升)

# 令之三斗，有餘二升
假2 = 3  # 假設的米數 (斗)
盈2 = Fraction(2, 10)  # 有餘 2 升，轉換為斗 (1斗 = 10升)

# 置所出率，盈、不足各居其下
率1 = 假1 + 不足1  # 第一假設的結果
率2 = 假2 + 盈2  # 第二假設的結果

# 令維乘所出率，并以為實
實 = (假1 * 率2) - (假2 * 率1)

# 并盈、不足為法
法 = 率2 - 率1

# 實如法而一
a = Fraction(實, 法)  # 5/2 (斗)
"""
Variable 'a' has wrong value. Expected: 5/2, Actual: 5/7"""
