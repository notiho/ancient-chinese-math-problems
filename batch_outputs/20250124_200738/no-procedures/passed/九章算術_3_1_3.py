"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

#----- content starts here -----
"""
Suppose there are a cow, a horse, and a sheep eating someone's crops. The crop owner demands 5 dou of millet as compensation.
The sheep owner says, "My sheep eats half as much as a horse."
The horse owner says, "My horse eats half as much as a cow."
Now, we want to fairly divide the compensation. How much should each pay?

Answer: The cow owner pays *a* dou, the horse owner pays *b* dou, and the sheep owner pays *c* sheng.
"""

from fractions import Fraction

# Total compensation in dou
total_compensation = 5

# Ratios of consumption:
# Sheep eats half as much as a horse
# Horse eats half as much as a cow
# Let the cow's consumption be 1 unit
cow_ratio = 1
horse_ratio = Fraction(1, 2) * cow_ratio
sheep_ratio = Fraction(1, 2) * horse_ratio

# Total ratio
total_ratio = cow_ratio + horse_ratio + sheep_ratio

# Calculate each owner's share
a = Fraction(cow_ratio, total_ratio) * total_compensation  # Cow owner's share in dou
b = Fraction(horse_ratio, total_ratio) * total_compensation  # Horse owner's share in dou
c = Fraction(sheep_ratio, total_ratio) * total_compensation * 10  # Sheep owner's share in sheng (1 dou = 10 sheng)

# Results
a, b, c#----- content ends here -----

"""
"""
