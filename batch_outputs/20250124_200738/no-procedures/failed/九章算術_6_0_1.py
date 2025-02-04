"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
This problem involves proportional distribution of grain and carts based on the number of households and the distance (in days) traveled by each county. The goal is to allocate the total grain (250,000 hu) and carts (10,000 carts) among the four counties proportionally.

### Problem Breakdown:
1. Each county's contribution is proportional to the product of its number of households and the distance (in days) traveled.
2. The total grain is 250,000 hu, and the total carts are 10,000 carts.
3. We calculate the proportional share for each county based on the above factors.

Here is the Python code to solve the problem:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"households": 10000, "days": 8},     # County A
    {"households": 9500, "days": 10},    # County B
    {"households": 12350, "days": 13},   # County C
    {"households": 12200, "days": 20},   # County D
]

# Total grain and carts
total_grain = 250000  # hu
total_carts = 10000   # carts

# Calculate the weight (households * days) for each county
weights = [county["households"] * county["days"] for county in counties]

# Total weight
total_weight = sum(weights)

# Calculate grain and carts for each county
results = []
for weight in weights:
    grain = Fraction(weight * total_grain, total_weight)
    carts = Fraction(weight * total_carts, total_weight)
    results.append({"grain": grain, "carts": carts})

# Output results
a, b = results[0]["grain"], results[0]["carts"]  # County A
c, d = results[1]["grain"], results[1]["carts"]  # County B
e, f = results[2]["grain"], results[2]["carts"]  # County C
g, h = results[3]["grain"], results[3]["carts"]  # County D

# Print the results
print(f"甲縣粟 {a}斛 ，車 {b}乘 。")
print(f"乙縣粟 {c}斛 ，車 {d}乘 。")
print(f"丙縣粟 {e}斛 ，車 {f}乘 。")
print(f"丁縣粟 {g}斛 ，車 {h}乘 。")
#----- content ends here -----


"""


### Explanation:
1. **Weights Calculation**: Each county's weight is calculated as `households * days`.
2. **Proportional Distribution**: The grain and carts are distributed proportionally based on the weights.
3. **Fraction Class**: The `Fraction` class is used to ensure exact calculations without floating-point errors.

### Example Output:
For the given data:
- 甲縣粟 `a` hu, 車 `b` carts.
- 乙縣粟 `c` hu, 車 `d` carts.
- 丙縣粟 `e` hu, 車 `f` carts.
- 丁縣粟 `g` hu, 車 `h` carts.

This approach ensures the distribution is fair and proportional to both the number of households and the distance traveled.
"""


"""
Variable 'a' has wrong value. Expected: 83100, Actual: 400000000/11591
Variable 'b' has wrong value. Expected: 3324, Actual: 16000000/11591
Variable 'c' has wrong value. Expected: 63175, Actual: 475000000/11591
Variable 'd' has wrong value. Expected: 2527, Actual: 19000000/11591
Variable 'e' has wrong value. Expected: 63175, Actual: 802750000/11591
Variable 'f' has wrong value. Expected: 2527, Actual: 32110000/11591
Variable 'g' has wrong value. Expected: 40550, Actual: 1220000000/11591
Variable 'h' has wrong value. Expected: 1622, Actual: 48800000/11591"""
