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
Suppose the original rice was 2 dou, then it is 2 sheng short. 
Suppose it was 3 dou, then there is an excess of 2 sheng.

The "excess and deficiency" method says: Place the output rates, with the excess and deficiency below them. 
Multiply the rates by their respective excess or deficiency, then add them to form the dividend. 
Add the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a remainder, simplify it. 
If the excess and deficiency are related to the same object, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the value of the object, and the divisor becomes the number of people.

Answer: *a* dou.
"""

from fractions import Fraction

# Known values
桶容量 = 10  # 10-dou bucket
舂後米 = 7  # 7 dou of rice obtained

# Hypotheses
假設1_米 = 2  # Suppose the original rice was 2 dou
假設1_不足 = Fraction(2, 10)  # 2 sheng short (1 dou = 10 sheng)

假設2_米 = 3  # Suppose the original rice was 3 dou
假設2_餘 = Fraction(2, 10)  # 2 sheng excess

# 盈不足術 calculations
# Multiply the rates by their respective excess or deficiency
實 = (假設1_米 * 假設2_餘) + (假設2_米 * 假設1_不足)

# Add the excess and deficiency to form the divisor
法 = 假設2_餘 + 假設1_不足

# Divide to find the original amount of rice
a = 實 / 法

# Output the result
a  # The original amount of rice in dou#----- content ends here -----

"""
"""
