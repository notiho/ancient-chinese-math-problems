"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing resources (粟 and 車) among four counties (甲, 乙, 丙, 丁) based on their population and distance. The solution involves proportional allocation using the given "衰" values.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_corn = 250000  # Total 粟 in 斛
total_carts = 10000  # Total 車 in 乘

# County data
counties = {
    "甲": {"households": 10000, "days": 8},
    "乙": {"households": 9500, "days": 10},
    "丙": {"households": 12350, "days": 13},
    "丁": {"households": 12200, "days": 20},
}

# Calculate 衰 values
for county, data in counties.items():
    data["衰"] = data["households"] * data["days"]

# Calculate total 衰
total_衰 = sum(data["衰"] for data in counties.values())

# Calculate 粟 and 車 for each county
for county, data in counties.items():
    data["車"] = Fraction(data["衰"], total_衰) * total_carts
    data["粟"] = data["車"] * 25  # Each cart carries 25 斛 of 粟

# Assign results to variables
a = counties["甲"]["粟"]
b = counties["甲"]["車"]
c = counties["乙"]["粟"]
d = counties["乙"]["車"]
e = counties["丙"]["粟"]
f = counties["丙"]["車"]
g = counties["丁"]["粟"]
h = counties["丁"]["車"]

# Results
a, b, c, d, e, f, g, h


"""


### Explanation:
1. **Input Data**:
   - Total 粟 (corn) is 250,000 斛.
   - Total 車 (carts) is 10,000 乘.
   - Each county has a number of households and a distance in days.

2. **衰 Calculation**:
   - For each county, 衰 is calculated as the product of the number of households and the distance in days.

3. **Proportional Allocation**:
   - The total 衰 is the sum of all counties' 衰 values.
   - Each county's share of carts is proportional to its 衰 value relative to the total 衰.
   - Each cart carries 25 斛 of 粟, so the 粟 for each county is calculated as carts × 25.

4. **Results**:
   - The results are stored in variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h` for 粟 and 車 for each county.

### Output:
The variables `a`, `b`, `c`, `d`, `e`, `f`, `g`, `h` contain the respective 粟 (in 斛) and 車 (in 乘) for counties 甲, 乙, 丙, 丁.
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
