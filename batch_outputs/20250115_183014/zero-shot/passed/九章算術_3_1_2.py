"""
今有牛、馬、羊食人苗。苗主責之粟五斗。羊主曰：「我羊食半馬。」馬主曰：「我馬食半牛。」今欲衰償之，問︰各出幾何？
術曰：置牛四、馬二、羊一，各自為列衰，副并為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：牛主出 a斗 。馬主出 b斗 。羊主出 c升 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining how much each animal owner should compensate (in units of grain) based on the amount of crops their animals consumed.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_grain = 5  # Total compensation in dou (斗)

# Ratios of consumption
cow_ratio = 4  # 牛
horse_ratio = 2  # 馬
sheep_ratio = 1  # 羊

# Total ratio
total_ratio = cow_ratio + horse_ratio + sheep_ratio

# Calculate the compensation for each owner
a = Fraction(total_grain * cow_ratio, total_ratio)  # 牛主出 a斗
b = Fraction(total_grain * horse_ratio, total_ratio)  # 馬主出 b斗
c = Fraction(total_grain * sheep_ratio, total_ratio) * 10  # 羊主出 c升 (1斗 = 10升)

# Results
a, b, c


"""


### Explanation:
1. The ratios of consumption are given as 4:2:1 for the cow, horse, and sheep, respectively.
2. The total compensation is 5 dou (斗).
3. The total ratio is the sum of the individual ratios: \( 4 + 2 + 1 = 7 \).
4. Each owner's compensation is calculated as their ratio divided by the total ratio, multiplied by the total compensation.
5. Since 1 dou = 10 sheng (升), the sheep's compensation is converted to sheng.

### Output:
- `a = Fraction(20, 7)` (牛主出 \( \frac{20}{7} \) 斗)
- `b = Fraction(10, 7)` (馬主出 \( \frac{10}{7} \) 斗)
- `c = Fraction(10, 7) * 10 = Fraction(100, 7)` (羊主出 \( \frac{100}{7} \) 升)
"""


"""
"""
