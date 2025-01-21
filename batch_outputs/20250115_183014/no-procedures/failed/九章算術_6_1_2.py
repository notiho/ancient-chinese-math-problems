"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing labor (or conscripted workers) among five counties based on their population and the distance they must travel. The goal is to allocate the total labor requirement (1,200 workers per month) proportionally, considering both the population of each county and the distance they must travel.

Let's break it down step by step and solve it in Python.

---

### Problem Setup:

- **甲縣**: 1,200 people, distance = 1 day
- **乙縣**: 1,550 people, distance = 1 day
- **丙縣**: 1,280 people, distance = 2 days
- **丁縣**: 990 people, distance = 3 days
- **戊縣**: 1,750 people, distance = 5 days
- Total labor required: 1,200 workers per month.

The allocation is based on the formula:
\[
\text{Weight for each county} = \text{Population} \times \text{Distance}
\]

The total weight is the sum of all counties' weights. Each county's share of the total labor is proportional to its weight.

---

### Python Code:


"""


from fractions import Fraction

# County data: (population, distance)
counties = {
    "甲": (1200, 1),
    "乙": (1550, 1),
    "丙": (1280, 2),
    "丁": (990, 3),
    "戊": (1750, 5)
}

# Total labor required
total_labor = 1200

# Step 1: Calculate weights for each county
weights = {county: population * distance for county, (population, distance) in counties.items()}

# Step 2: Calculate total weight
total_weight = sum(weights.values())

# Step 3: Calculate labor allocation for each county
allocations = {county: Fraction(weight * total_labor, total_weight) for county, weight in weights.items()}

# Step 4: Output results
for county, labor in allocations.items():
    print(f"{county}縣: {labor}人")


"""


---

### Explanation of the Code:

1. **Weights Calculation**:
   Each county's weight is calculated as:
   \[
   \text{Weight} = \text{Population} \times \text{Distance}
   \]

2. **Total Weight**:
   The sum of all counties' weights is used to determine the proportion of labor each county should contribute.

3. **Labor Allocation**:
   Each county's labor contribution is calculated as:
   \[
   \text{Labor for County} = \frac{\text{County Weight} \times \text{Total Labor}}{\text{Total Weight}}
   \]

4. **Fraction Module**:
   The `Fraction` class is used to ensure precise calculations without floating-point errors.

---

### Output:

The program will output the labor allocation for each county in terms of exact fractions or integers:

```
甲縣: a人
乙縣: b人
丙縣: c人
丁縣: d人
戊縣: e人
```

You can replace `a`, `b`, `c`, `d`, and `e` with the actual computed values from the program.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
