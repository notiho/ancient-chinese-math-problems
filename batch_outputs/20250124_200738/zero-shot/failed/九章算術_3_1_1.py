"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much each animal's owner should compensate for the crops eaten, given the relationships between the animals' consumption.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given relationships:
# Sheep eats half as much as a horse.
# Horse eats half as much as a cow.

# Let the units of consumption be:
# Cow = 4 units
# Horse = 2 units
# Sheep = 1 unit

# Total compensation is 5斗 (5 dou).
total_compensation = 5

# The proportional contributions are based on the units:
cow_units = 4
horse_units = 2
sheep_units = 1

# Total units:
total_units = cow_units + horse_units + sheep_units

# Calculate the compensation for each:
a = Fraction(cow_units, total_units) * total_compensation  # Compensation for the cow's owner
b = Fraction(horse_units, total_units) * total_compensation  # Compensation for the horse's owner
c = Fraction(sheep_units, total_units) * total_compensation  # Compensation for the sheep's owner

# Results:
a  # Cow owner's compensation in 斗
b  # Horse owner's compensation in 斗
c  # Sheep owner's compensation in 斗
#----- content ends here -----


"""


### Explanation:
1. The problem states that the sheep eats half as much as a horse, and the horse eats half as much as a cow. Thus, the consumption ratio is:
   - Cow: 4 units
   - Horse: 2 units
   - Sheep: 1 unit

2. The total compensation is 5斗 (5 dou). We distribute this compensation proportionally based on the consumption units.

3. Using the `Fraction` class ensures that the results are accurate and expressed as fractions where necessary.

### Output:
- `a = Fraction(20, 7)` (Cow owner's compensation in 斗)
- `b = Fraction(10, 7)` (Horse owner's compensation in 斗)
- `c = Fraction(5, 7)` (Sheep owner's compensation in 斗)
"""


"""
Variable 'c' has wrong value. Expected: 50/7, Actual: 5/7"""
