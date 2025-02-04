"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a斗 。
"""

"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
When the bucket is filled with millet and pounded, it produces 7 dou of rice.
Question: how much rice was originally present?

The procedure says: Use the "excess and deficiency" method to solve it.
Suppose the original rice is 2 dou, then it is deficient by 2 sheng.
Suppose it is 3 dou, then it is in excess by 2 sheng.

The "excess and deficiency" method says: Place the given rates, with the excess and deficiency below them respectively.
Multiply the rates by their respective excess or deficiency, and add them together to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
If the excess and deficiency are related to the same object, subtract the smaller rate from the larger rate, and simplify the divisor and dividend accordingly.
The dividend becomes the price of the object, and the divisor becomes the number of people.

Answer: *a* dou.
"""

from fractions import Fraction

# 假令故米二斗，不足二升
假設1_米 = 2  # 斗
不足1 = Fraction(2, 10)  # 2升 = 2/10斗

# 令之三斗，有餘二升
假設2_米 = 3  # 斗
有餘2 = Fraction(2, 10)  # 2升 = 2/10斗

# 置所出率，盈、不足各居其下
率1 = 假設1_米
率2 = 假設2_米

# 令維乘所出率，并以為實
實 = (率1 * 有餘2) + (率2 * 不足1)

# 并盈、不足為法
法 = 有餘2 + 不足1

# 實如法而一
a = Fraction(實, 法)  # 結果是原來的米數，單位是斗
"""
"""
