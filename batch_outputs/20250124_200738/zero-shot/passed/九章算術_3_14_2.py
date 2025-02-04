"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves proportional reasoning to determine how much "縑" (a type of silk fabric) can be obtained from a given amount of "絲" (raw silk). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
silk_1 = Fraction(14)  # 14斤 of raw silk
fabric_1 = Fraction(10)  # 10斤 of fabric obtained
silk_2 = Fraction(45) + Fraction(8, 16)  # 45斤 8兩 of raw silk (1斤 = 16兩)

# Proportional calculation
a = (fabric_1 * silk_2) / silk_1  # Calculate the amount of fabric obtained

# Result
a  # a is the amount of fabric in 斤
#----- content ends here -----


"""


### Explanation:
1. **Input Data**:
   - `silk_1` is the initial amount of raw silk (14斤).
   - `fabric_1` is the amount of fabric obtained from `silk_1` (10斤).
   - `silk_2` is the new amount of raw silk (45斤 8兩, where 1斤 = 16兩, so 8兩 = 8/16 = 1/2斤).

2. **Proportional Calculation**:
   - The relationship between raw silk and fabric is proportional.
   - Using the formula from the problem: `(fabric_1 * silk_2) / silk_1`.

3. **Output**:
   - The result `a` represents the amount of fabric obtained from `silk_2`.

### Final Answer:
The variable `a` will contain the amount of fabric in 斤 as a `Fraction`.
"""


"""
"""
