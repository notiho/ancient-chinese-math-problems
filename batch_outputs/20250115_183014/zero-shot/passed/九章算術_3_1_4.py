"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much each animal's owner should pay based on their respective contributions to the damage.

Here is the Python code:


"""


from fractions import Fraction

# Given values
total_damage = 5  # in dou (斗)
cow_contribution = 4
horse_contribution = 2
sheep_contribution = 1

# Total contribution as the sum of all contributions
total_contribution = cow_contribution + horse_contribution + sheep_contribution

# Calculate each owner's share of the damage
a = Fraction(cow_contribution, total_contribution) * total_damage  # Cow owner's share in dou
b = Fraction(horse_contribution, total_contribution) * total_damage  # Horse owner's share in dou
c = Fraction(sheep_contribution, total_contribution) * total_damage  # Sheep owner's share in dou

# Convert sheep's share to sheng (升), as 1 dou = 10 sheng
c = c * 10  # Sheep owner's share in sheng

# Results
a, b, c


"""


### Explanation:
1. The total contribution is calculated as the sum of the contributions of the cow, horse, and sheep (4, 2, and 1, respectively).
2. Each owner's share of the damage is proportional to their animal's contribution.
3. The sheep's share is converted from dou to sheng because 1 dou = 10 sheng.

### Solution:
- `a` (Cow owner's share) = 2 dou
- `b` (Horse owner's share) = 1 dou
- `c` (Sheep owner's share) = 10 sheng
"""


"""
"""
