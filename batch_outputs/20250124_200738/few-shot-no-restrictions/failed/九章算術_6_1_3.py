"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing labor (soldiers) among five counties based on their distance (travel days) and the number of people available in each county. The goal is to calculate how many soldiers each county should contribute, considering the distance and population.

Here is the solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
# Format: (population, travel_days)
counties = {
    "甲": (1200, 1),
    "乙": (1550, 1),
    "丙": (1280, 2),
    "丁": (990, 3),
    "戊": (1750, 5),
}

# Total soldiers required per month
total_soldiers = 1200

# Step 1: Calculate衰 (weight) for each county
# 衰 = population * (travel_days + 1)
weights = {county: population * (travel_days + 1) for county, (population, travel_days) in counties.items()}

# Step 2: Calculate the 法 (sum of weights)
法 = sum(weights.values())

# Step 3: Calculate the 实 (actual contribution) for each county
# 实 = (total_soldiers * weight) / 法
results = {county: Fraction(total_soldiers * weight, 法) for county, weight in weights.items()}

# Step 4: Output results
for county, contribution in results.items():
    print(f"{county}縣: {contribution}人")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: Each county has a population and a number of travel days. The travel days are increased by 1 to account for the distance factor.
2. **Weights (衰)**: The weight for each county is calculated as `population * (travel_days + 1)`.
3. **法 (Sum of Weights)**: The total weight is the sum of all individual weights.
4. **Actual Contribution (实)**: Each county's contribution is proportional to its weight, calculated as `(total_soldiers * weight) / 法`.
5. **Output**: The result is displayed as the number of soldiers each county should contribute.

### Example Output:
For the given data:
- 甲縣: `a` 人
- 乙縣: `b` 人
- 丙縣: `c` 人
- 丁縣: `d` 人
- 戊縣: `e` 人

The exact values will be fractions or integers depending on the calculation.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
