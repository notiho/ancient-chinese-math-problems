"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing resources (粟 and 車) among four counties based on their respective household numbers and travel days. The solution uses proportional distribution based on the given rules.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_grain = 250000  # Total 粟 in 斛
total_carts = 10000   # Total 車
counties = [
    {"households": 10000, "days": 8},   # 甲縣
    {"households": 9500, "days": 10},  # 乙縣
    {"households": 12350, "days": 13}, # 丙縣
    {"households": 12200, "days": 20}  # 丁縣
]

# Step 1: Calculate衰 for each county
for county in counties:
    county["衰"] = county["households"] * county["days"]

# Step 2: Calculate the total衰
total_衰 = sum(county["衰"] for county in counties)

# Step 3: Calculate the proportion of carts and grain for each county
for county in counties:
    county["cart_fraction"] = Fraction(county["衰"], total_衰)
    county["carts"] = county["cart_fraction"] * total_carts
    county["grain"] = county["cart_fraction"] * total_grain

# Assign results to variables
a = counties[0]["grain"]
b = counties[0]["carts"]
c = counties[1]["grain"]
d = counties[1]["carts"]
e = counties[2]["grain"]
f = counties[2]["carts"]
g = counties[3]["grain"]
h = counties[3]["carts"]

# Results
a, b, c, d, e, f, g, h
#----- content ends here -----


"""


### Explanation:
1. **Input Data**: The number of households and travel days for each county are given.
2. **衰 Calculation**: Each county's "衰" is calculated as the product of its households and travel days.
3. **Total 衰**: The sum of all counties' "衰" values is computed.
4. **Proportions**: Each county's proportion of carts and grain is determined by dividing its "衰" by the total "衰".
5. **Final Distribution**: Using the proportions, the number of carts and grain for each county is calculated.

### Output:
The variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h` represent the grain (in 斛) and carts (in 車) for counties 甲, 乙, 丙, and 丁 respectively.
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
