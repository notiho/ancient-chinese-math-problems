"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing resources (粟 and 車) among four counties (甲, 乙, 丙, 丁) based on their respective household numbers and travel days. The solution will compute the values of the unknowns \( a, b, c, d, e, f, g, h \).

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_grain = 250000  # Total 粟 in 斛
total_carts = 10000   # Total 車
grain_per_cart = 25   # 粟 per 車 in 斛

# County data: (households, travel days)
county_data = {
    "甲": (10000, 8),
    "乙": (9500, 10),
    "丙": (12350, 13),
    "丁": (12200, 20)
}

# Calculate衰 for each county
衰 = {
    "甲": county_data["甲"][0] * county_data["甲"][1],
    "乙": county_data["乙"][0] * county_data["乙"][1],
    "丙": county_data["丙"][0] * county_data["丙"][1],
    "丁": county_data["丁"][0] * county_data["丁"][1]
}

# Total衰
total_衰 = sum(衰.values())

# Calculate the number of carts (車) for each county
b = Fraction(total_carts * 衰["甲"], total_衰)
d = Fraction(total_carts * 衰["乙"], total_衰)
f = Fraction(total_carts * 衰["丙"], total_衰)
h = Fraction(total_carts * 衰["丁"], total_衰)

# Calculate the amount of grain (粟) for each county
a = b * grain_per_cart
c = d * grain_per_cart
e = f * grain_per_cart
g = h * grain_per_cart

# Results
a, b, c, d, e, f, g, h


"""


### Explanation of the Code:
1. **Input Data**:
   - Total grain (粟) and total carts (車) are given.
   - Each county's household numbers and travel days are provided.

2. **衰 Calculation**:
   - For each county, \( \text{衰} = \text{households} \times \text{travel days} \).

3. **Total 衰**:
   - Sum up the 衰 values for all counties.

4. **Carts Distribution**:
   - The number of carts for each county is proportional to its 衰 value:
     \[
     \text{carts for a county} = \frac{\text{total carts} \times \text{county 衰}}{\text{total 衰}}
     \]

5. **Grain Distribution**:
   - The amount of grain for each county is calculated as:
     \[
     \text{grain for a county} = \text{carts for the county} \times \text{grain per cart}
     \]

6. **Output**:
   - The variables \( a, b, c, d, e, f, g, h \) represent the grain and carts for each county.

### Results:
The results are stored in the variables \( a, b, c, d, e, f, g, h \), which represent:
- \( a \): Grain for 甲 county (in 斛)
- \( b \): Carts for 甲 county
- \( c \): Grain for 乙 county (in 斛)
- \( d \): Carts for 乙 county
- \( e \): Grain for 丙 county (in 斛)
- \( f \): Carts for 丙 county
- \( g \): Grain for 丁 county (in 斛)
- \( h \): Carts for 丁 county
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
