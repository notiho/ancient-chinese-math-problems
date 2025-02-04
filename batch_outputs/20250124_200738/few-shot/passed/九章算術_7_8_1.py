"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
When the bucket is filled with millet and pounded, 7 dou of rice are obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "excess and deficiency" method to solve it.
Suppose the original rice was 2 dou, then it is deficient by 2 sheng.
Suppose it was 3 dou, then it is in excess by 2 sheng.

The "excess and deficiency" method says: Place the rates of output, with the excess and deficiency below them respectively.
Multiply the rates of output by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result.
If there is a fraction, simplify it.
If the excess and deficiency are associated with the same item, subtract the smaller from the larger and simplify the divisor and dividend accordingly.
The dividend becomes the value of the item, and the divisor becomes the number of people.

Answer: *a* dou.
"""

from fractions import Fraction

# 假令故米二斗，不足二升
假設1_斗 = 2
不足1_升 = Fraction(2, 10)  # 2升 = 2/10斗

# 令之三斗，有餘二升
假設2_斗 = 3
有餘2_升 = Fraction(2, 10)  # 2升 = 2/10斗

# 置所出率，盈、不足各居其下
率1 = 假設1_斗
率2 = 假設2_斗

# 令維乘所出率，并以為實
實 = (率1 * 有餘2_升) + (率2 * 不足1_升)

# 并盈、不足為法
法 = 有餘2_升 + 不足1_升

# 實如法而一
a = Fraction(實, 法)  # 原來的米數 (斗)#----- content ends here -----

"""
"""
