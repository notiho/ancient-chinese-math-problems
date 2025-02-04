"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing resources (粟 and 車) among four counties (甲, 乙, 丙, 丁) based on their population and distance. The solution uses the "均輸術" (equal distribution method) to calculate the values of the unknowns.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_cars = 10000  # Total cars
total_grain = 250000  # Total grain in 斛
grain_per_car = 25  # Grain per car in 斛

# County data: (households, travel days)
counties = {
    "甲": (10000, 8),
    "乙": (9500, 10),
    "丙": (12350, 13),
    "丁": (12200, 20)
}

# Calculate衰 for each county
衰 = {
    "甲": counties["甲"][0] * counties["甲"][1],
    "乙": counties["乙"][0] * counties["乙"][1],
    "丙": counties["丙"][0] * counties["丙"][1],
    "丁": counties["丁"][0] * counties["丁"][1]
}

# Total衰
total_衰 = sum(衰.values())

# Calculate cars and grain for each county
a = Fraction(衰["甲"] * total_grain, total_衰)  # 粟 for 甲
b = Fraction(衰["甲"] * total_cars, total_衰)  # 車 for 甲

c = Fraction(衰["乙"] * total_grain, total_衰)  # 粟 for 乙
d = Fraction(衰["乙"] * total_cars, total_衰)  # 車 for 乙

e = Fraction(衰["丙"] * total_grain, total_衰)  # 粟 for 丙
f = Fraction(衰["丙"] * total_cars, total_衰)  # 車 for 丙

g = Fraction(衰["丁"] * total_grain, total_衰)  # 粟 for 丁
h = Fraction(衰["丁"] * total_cars, total_衰)  # 車 for 丁

# Results
a, b, c, d, e, f, g, h


"""


### Explanation:
1. **Input Data**:
   - Each county has a number of households and travel days.
   - Total resources (grain and cars) are given.

2. **Calculate 衰**:
   - 衰 for each county is calculated as `households * travel days`.

3. **Total 衰**:
   - Sum the 衰 values for all counties.

4. **Distribute Resources**:
   - Grain and cars are distributed proportionally based on each county's 衰.

5. **Output**:
   - The variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h` represent the grain (粟) and cars (車) allocated to each county.

### Results:
The results will be in the form of fractions, which can be converted to decimals if needed.
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
