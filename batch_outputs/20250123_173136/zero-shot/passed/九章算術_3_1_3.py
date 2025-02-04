"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much each animal's owner should compensate for the crops eaten, given the relationships between the animals' consumption.

Here is the Python code:


"""


from fractions import Fraction

# Given relationships:
# Sheep eats half as much as a horse.
# Horse eats half as much as a cow.

# Let the units of consumption be:
cow = 4  # Cow's consumption is 4 units.
horse = 2  # Horse's consumption is half of a cow's consumption.
sheep = 1  # Sheep's consumption is half of a horse's consumption.

# Total compensation required is 5斗 (5 dou).
total_compensation = 5

# Calculate the proportion of compensation for each animal:
total_units = cow + horse + sheep  # Total units of consumption.
unit_value = Fraction(total_compensation, total_units)  # Value of one unit in dou.

# Calculate the compensation for each owner:
a = cow * unit_value  # Compensation for the cow's owner in dou.
b = horse * unit_value  # Compensation for the horse's owner in dou.
c = sheep * unit_value * 10  # Compensation for the sheep's owner in 升 (1 dou = 10 升).

# Results:
a, b, c


"""


### Explanation:
1. The cow, horse, and sheep have consumption ratios of 4:2:1, respectively.
2. The total compensation required is 5斗 (dou).
3. We calculate the value of one unit of consumption by dividing the total compensation by the total units of consumption.
4. Each owner's compensation is then calculated by multiplying their respective consumption units by the unit value.
5. The sheep's compensation is converted from dou to 升 (1 dou = 10 升).

### Output:
The variables `a`, `b`, and `c` will contain the compensation for the cow's owner (in dou), the horse's owner (in dou), and the sheep's owner (in 升), respectively.
"""


"""
"""
