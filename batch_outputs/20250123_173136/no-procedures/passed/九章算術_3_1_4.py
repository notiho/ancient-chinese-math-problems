"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
Suppose there are cattle, horses, and sheep that ate someone's crops. The owner of the crops demands 5 dou of millet as compensation.
The sheep owner says, "My sheep eats half as much as a horse."
The horse owner says, "My horse eats half as much as a cow."
Now, we want to proportionally divide the compensation. How much does each owner pay?

Answer: The cattle owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

from fractions import Fraction

# Total compensation in dou
total_compensation = 5

# Ratios of consumption:
# Let the cow's consumption be 1 unit
cow_consumption = 1
horse_consumption = Fraction(1, 2) * cow_consumption
sheep_consumption = Fraction(1, 2) * horse_consumption

# Total consumption ratio
total_consumption = cow_consumption + horse_consumption + sheep_consumption

# Calculate each owner's share of the compensation
a = Fraction(cow_consumption, total_consumption) * total_compensation  # Cow owner's share in dou
b = Fraction(horse_consumption, total_consumption) * total_compensation  # Horse owner's share in dou
c = Fraction(sheep_consumption, total_consumption) * total_compensation * 10  # Sheep owner's share in sheng (1 dou = 10 sheng)

# Output the results
a, b, c
"""
"""
