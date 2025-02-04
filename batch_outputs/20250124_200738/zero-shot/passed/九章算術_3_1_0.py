"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much each owner (cow, horse, sheep) should compensate for the damage caused by their animals eating crops. The relationships between the animals' consumption are given, and the total compensation is 5斗 (dou).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let the compensation for the cow, horse, and sheep be a, b, and c respectively.
# According to the problem:
# 1. A sheep eats half as much as a horse.
# 2. A horse eats half as much as a cow.
# 3. The total compensation is 5斗.

# Assign relative weights based on the problem:
# Cow = 4 units, Horse = 2 units, Sheep = 1 unit.
cow_weight = 4
horse_weight = 2
sheep_weight = 1

# Total weight is the sum of all weights.
total_weight = cow_weight + horse_weight + sheep_weight

# Each unit corresponds to a fraction of the total compensation.
unit_compensation = Fraction(5, total_weight)

# Calculate the compensation for each:
a = cow_weight * unit_compensation  # Compensation for the cow owner
b = horse_weight * unit_compensation  # Compensation for the horse owner
c = sheep_weight * unit_compensation  # Compensation for the sheep owner

# Convert c to 升 (1斗 = 10升)
c = c * 10

# Results:
a  # Compensation for the cow owner in 斗
b  # Compensation for the horse owner in 斗
c  # Compensation for the sheep owner in 升
#----- content ends here -----


"""


### Explanation of the Solution:
1. The weights of the cow, horse, and sheep are given as 4, 2, and 1 respectively.
2. The total weight is the sum of these weights: \( 4 + 2 + 1 = 7 \).
3. Each unit of weight corresponds to \( \frac{5}{7} \)斗 of compensation.
4. The compensation for each owner is calculated by multiplying their respective weight by \( \frac{5}{7} \).
5. The sheep's compensation is converted from 斗 to 升 by multiplying by 10 (since 1斗 = 10升).

### Final Values:
- \( a = \frac{20}{7} \)斗
- \( b = \frac{10}{7} \)斗
- \( c = \frac{10}{7} \times 10 = \frac{100}{7} \)升
"""


"""
"""
