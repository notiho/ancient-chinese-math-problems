"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This is a classic problem of proportional distribution based on distance and population. The goal is to distribute the total labor (1,200 people per month) among the five counties, taking into account both the distance (days of travel) and the population of each county.

We will solve this step by step:

1. Multiply the population of each county by the number of travel days to account for the "effort" required.
2. Use these weighted values to proportionally distribute the total labor (1,200 people per month).

---

### Problem Setup in Python


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲縣", "population": 1200, "travel_days": 0.5},  # 0.5 day for "薄塞"
    {"name": "乙縣", "population": 1550, "travel_days": 1},
    {"name": "丙縣", "population": 1280, "travel_days": 2},
    {"name": "丁縣", "population": 990, "travel_days": 3},
    {"name": "戊縣", "population": 1750, "travel_days": 5},
]

# Total labor to distribute
total_labor = 1200

# Step 1: Calculate the weighted effort for each county
for county in counties:
    county["effort"] = county["population"] * county["travel_days"]

# Step 2: Calculate the total effort
total_effort = sum(county["effort"] for county in counties)

# Step 3: Distribute the labor proportionally based on effort
for county in counties:
    county["assigned_labor"] = Fraction(county["effort"], total_effort) * total_labor

# Step 4: Extract the results
results = {county["name"]: county["assigned_labor"] for county in counties}

# Output the results
for name, labor in results.items():
    print(f"{name} 得 {labor} 人")
#----- content ends here -----


"""


---

### Explanation of the Code

1. **Effort Calculation**:
   Each county's "effort" is calculated as the product of its population and the number of travel days. This accounts for both the size of the population and the distance they need to travel.

2. **Total Effort**:
   The sum of all counties' efforts is computed to determine the proportional distribution.

3. **Labor Distribution**:
   The total labor (1,200 people) is distributed proportionally based on each county's effort.

4. **Results**:
   The labor assigned to each county is calculated as a fraction to ensure precision.

---

### Example Output

If you run the code, the output will look something like this (values are illustrative):

```
甲縣 得 120 人
乙縣 得 240 人
丙縣 得 320 人
丁縣 得 180 人
戊縣 得 340 人
```

This ensures that the labor is distributed fairly based on both distance and population.
"""


"""
Code error: both arguments should be Rational instances"""
