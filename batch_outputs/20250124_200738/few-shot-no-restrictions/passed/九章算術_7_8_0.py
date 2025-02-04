"""
今有米在十斗桶中，不知其數。滿中添粟而舂之，得米七斗。問︰故米幾何？
術曰：以盈不足術求之，假令故米二斗，不足二升。令之三斗，有餘二升。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is an unknown amount of rice in a 10-dou bucket. 
After filling the bucket with millet and pounding it, 7 dou of rice is obtained.
Question: how much rice was originally in the bucket?

The procedure says: Use the "excess and deficiency" method to solve it.
Suppose the original rice was 2 dou, but it was short by 2 sheng.
Suppose it was 3 dou, but it exceeded by 2 sheng.

The "excess and deficiency" method says: Place the output rates, with the excess and deficiency below them.
Multiply the rates by the respective excess or deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
If the excess and deficiency are related to the same object, place the rates, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the value of the object, and the divisor becomes the number of people.

Answer: *a* dou.
"""

from fractions import Fraction

# Known values
桶容量 = 10  # 10-dou bucket
舂後米 = 7  # 7 dou of rice after pounding

# Assumptions for the "excess and deficiency" method
假設1_米 = 2  # Assume 2 dou of rice
假設1_不足 = Fraction(2, 10)  # Short by 2 sheng (1 dou = 10 sheng)

假設2_米 = 3  # Assume 3 dou of rice
假設2_盈餘 = Fraction(2, 10)  # Exceeded by 2 sheng

# 盈不足術 calculations
# Dividend (實)
實 = (假設1_米 * 假設2_盈餘) + (假設2_米 * 假設1_不足)

# Divisor (法)
法 = 假設2_盈餘 + 假設1_不足

# Result (original rice amount)
a = 實 / 法

# Output
a#----- content ends here -----

"""
"""
