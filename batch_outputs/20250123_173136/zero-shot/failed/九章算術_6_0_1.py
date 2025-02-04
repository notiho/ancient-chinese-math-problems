"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
To solve this problem, we will calculate the distribution of grain ("粟") and carts ("車") for each county based on the given data and the method described in the problem. Here's the Python code to compute the values:


"""


from fractions import Fraction

# Given data
total_grain = 250000  # Total grain in hu (斛)
total_carts = 10000   # Total carts (車)

# County data: (households, travel days)
county_data = {
    "甲": (10000, 8),
    "乙": (9500, 10),
    "丙": (12350, 13),
    "丁": (12200, 20)
}

# Calculate the "衰" (weight) for each county
weights = {
    "甲": Fraction(10000 * 8, 1),
    "乙": Fraction(9500 * 10, 1),
    "丙": Fraction(12350 * 13, 1),
    "丁": Fraction(12200 * 20, 1)
}

# Sum of weights
total_weight = sum(weights.values())

# Calculate the grain and carts for each county
a = weights["甲"] / total_weight * total_grain  # Grain for 甲
b = weights["甲"] / total_weight * total_carts  # Carts for 甲

c = weights["乙"] / total_weight * total_grain  # Grain for 乙
d = weights["乙"] / total_weight * total_carts  # Carts for 乙

e = weights["丙"] / total_weight * total_grain  # Grain for 丙
f = weights["丙"] / total_weight * total_carts  # Carts for 丙

g = weights["丁"] / total_weight * total_grain  # Grain for 丁
h = weights["丁"] / total_weight * total_carts  # Carts for 丁

# Results
a, b, c, d, e, f, g, h


"""


### Explanation of the Code:
1. **Input Data**:
   - Total grain (`total_grain`) and total carts (`total_carts`) are given.
   - Each county's data includes the number of households and travel days.

2. **Weights Calculation**:
   - The weight for each county is calculated as the product of the number of households and travel days.

3. **Proportional Distribution**:
   - The grain and carts are distributed proportionally to the weights of each county.

4. **Output Variables**:
   - `a`, `b`: Grain and carts for 甲 county.
   - `c`, `d`: Grain and carts for 乙 county.
   - `e`, `f`: Grain and carts for 丙 county.
   - `g`, `h`: Grain and carts for 丁 county.

The results are stored in the variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, and `h`.
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
