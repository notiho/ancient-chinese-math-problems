"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
To solve this problem, we need to calculate how much silk fabric ("縑") can be obtained from a given weight of raw silk ("絲"). The problem provides a ratio based on the first scenario: 14斤 of raw silk yields 10斤 of silk fabric. Using this ratio, we can compute the amount of silk fabric obtained from 45斤8兩 of raw silk.

In traditional Chinese units:
- 1斤 = 16兩.

Let's translate the problem into Python code:


"""


from fractions import Fraction

# Given data
raw_silk_1 = Fraction(14)  # 14斤
silk_fabric_1 = Fraction(10)  # 10斤
raw_silk_2 = Fraction(45) + Fraction(8, 16)  # 45斤8兩 (convert 8兩 to fraction of 斤)

# Ratio of silk fabric to raw silk
ratio = silk_fabric_1 / raw_silk_1

# Calculate the amount of silk fabric for the second case
a = ratio * raw_silk_2

# Result
a  # This is the amount of silk fabric in 斤


"""


The variable `a` will contain the amount of silk fabric obtained from 45斤8兩 of raw silk.
"""


"""
"""
