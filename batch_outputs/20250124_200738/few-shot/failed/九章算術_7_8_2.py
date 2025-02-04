"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
When the bucket is filled with millet and pounded, it produces 7 dou of rice. 
Question: how much rice was originally in the bucket?

The procedure says: Use the "excess and deficiency" method to solve it. 
Suppose the original rice was 2 dou, then it is deficient by 2 sheng. 
Suppose it was 3 dou, then it is in excess by 2 sheng.

The "excess and deficiency" method says: Place the rates of production, with the excess and deficiency below them, respectively. 
Multiply the rates of production by the respective excess or deficiency, and add them together to form the dividend. 
Add the excess and deficiency together to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a fraction, simplify it. 
If the excess and deficiency correspond to the same item being purchased, subtract the smaller rate from the larger rate, and simplify the divisor and dividend accordingly. 
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* dou.
"""

# 假令故米二斗，不足二升
假設1_斗 = 2
不足1_升 = 2 / 10  # 2升 = 2/10斗

# 令之三斗，有餘二升
假設2_斗 = 3
有餘2_升 = 2 / 10  # 2升 = 2/10斗

# 盈不足術曰：置所出率，盈、不足各居其下
率1 = 假設1_斗
率2 = 假設2_斗
不足 = 不足1_升
有餘 = 有餘2_升

# 令維乘所出率，并以為實
實 = (率1 * 有餘) + (率2 * 不足)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # 原來的米數 in 斗#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
