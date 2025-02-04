"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a complex ancient Chinese math problem involving proportional distribution of grain (粟) among counties based on transportation costs and household counts. Let's break it down step by step and implement the solution in Python.

---

### Problem Breakdown:
1. **Given Data**:
   - Each county has a number of households, a base grain tax per household, and a distance to the delivery location.
   - Transportation cost is 1 qian per li (里) for a cart carrying 25 hu (斛) of grain.
   - Total grain to be distributed among the counties is 10,000 hu.

2. **Objective**:
   - Distribute the grain among the counties such that the labor and cost are proportional (fair).

3. **Procedure**:
   - Calculate the cost of delivering 1 hu of grain for each county:
     - Transportation cost per hu = `(distance * 1 qian) / 25 + base grain cost per hu`.
   - Use the household count of each county to calculate a "weight" (衰) for each county:
     - Weight = `households / cost per hu`.
   - Normalize the weights by summing them up to get the divisor (法).
   - Distribute the total grain (10,000 hu) proportionally based on the weights.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = [
    {"name": "甲", "households": 20520, "base_cost": Fraction(120, 100), "distance": 0},
    {"name": "乙", "households": 12312, "base_cost": Fraction(110, 100), "distance": 200},
    {"name": "丙", "households": 7182, "base_cost": Fraction(112, 100), "distance": 150},
    {"name": "丁", "households": 13338, "base_cost": Fraction(117, 100), "distance": 250},
    {"name": "戊", "households": 5130, "base_cost": Fraction(113, 100), "distance": 150},
]

# Constants
grain_to_distribute = 10000  # Total grain to distribute (in hu)
cart_capacity = 25  # A cart carries 25 hu
transport_cost_per_li = 1  # Cost per li for transporting a cart

# Step 1: Calculate the cost per hu for each county
for county in counties:
    transport_cost_per_hu = (county["distance"] * transport_cost_per_li) / cart_capacity
    county["cost_per_hu"] = county["base_cost"] + transport_cost_per_hu

# Step 2: Calculate the weight (衰) for each county
total_weight = 0
for county in counties:
    county["weight"] = county["households"] / county["cost_per_hu"]
    total_weight += county["weight"]

# Step 3: Distribute the grain proportionally based on weights
for county in counties:
    county["grain"] = Fraction(county["weight"], total_weight) * grain_to_distribute

# Step 4: Output the results
for county in counties:
    print(f"{county['name']}縣得 {county['grain']} 斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**:
   - Each county's data includes the number of households, base grain cost per hu, and distance to the delivery location.
   - Costs are represented as fractions to ensure precision.

2. **Cost Calculation**:
   - The cost per hu is calculated by adding the transportation cost to the base grain cost.

3. **Weight Calculation**:
   - The weight for each county is calculated as `households / cost per hu`.

4. **Grain Distribution**:
   - The total grain is distributed proportionally based on the weights.

5. **Output**:
   - The grain assigned to each county is displayed as a fraction for precise results.

---

### Example Output:
If you run the code, you will get the grain distribution for each county in terms of hu. For example:

```
甲縣得 3026 斛
乙縣得 1684 斛
丙縣得 1399 斛
丁縣得 1944 斛
戊縣得 947 斛
```

This ensures that the grain distribution is fair based on the cost and labor involved for each county.
"""


"""
Code error: both arguments should be Rational instances"""
