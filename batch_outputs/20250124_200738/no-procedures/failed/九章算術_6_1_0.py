"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This is a classic problem of proportional distribution based on distance and population. The goal is to distribute the monthly labor quota of 1200 people among five counties, taking into account both the distance (number of days traveled) and the population of each county.

Here is the solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = {
    "甲": {"population": 1200, "distance": 1},
    "乙": {"population": 1550, "distance": 1},
    "丙": {"population": 1280, "distance": 2},
    "丁": {"population": 990, "distance": 3},
    "戊": {"population": 1750, "distance": 5},
}

# Total labor quota for one month
total_quota = 1200

# Calculate the weighted contribution for each county
weights = {}
for county, data in counties.items():
    weights[county] = data["population"] * data["distance"]

# Calculate the total weight
total_weight = sum(weights.values())

# Distribute the labor quota proportionally
results = {}
for county, weight in weights.items():
    results[county] = Fraction(weight * total_quota, total_weight)

# Output the results
a = results["甲"]
b = results["乙"]
c = results["丙"]
d = results["丁"]
e = results["戊"]

print(f"甲縣 {a}人")
print(f"乙縣 {b}人")
print(f"丙縣 {c}人")
print(f"丁縣 {d}人")
print(f"戊縣 {e}人")
#----- content ends here -----


"""


### Explanation:
1. **Population and Distance**: Each county has a population and a distance (in days of travel). The labor contribution is proportional to the product of these two factors.
2. **Weights**: The weight for each county is calculated as `population * distance`.
3. **Total Weight**: The sum of all weights is used as the denominator for proportional distribution.
4. **Quota Distribution**: Each county's share of the labor quota is calculated as `(county_weight / total_weight) * total_quota`.

This ensures that the labor is distributed fairly based on both population and distance.
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 144000/1703
Variable 'b' has wrong value. Expected: 286, Actual: 186000/1703
Variable 'c' has wrong value. Expected: 228, Actual: 307200/1703
Variable 'd' has wrong value. Expected: 171, Actual: 356400/1703
Variable 'e' has wrong value. Expected: 286, Actual: 1050000/1703"""
