"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a complex problem involving proportional distribution of grain (粟) among five counties based on transportation costs and household counts, ensuring equalized labor and expense. Let's break it down step by step and encode it in Python.

---

### Problem Breakdown:
1. **Given Data**:
   - Each county has a number of households, a base grain cost per hu (斛), and a distance to the delivery location.
   - Transportation cost is calculated based on distance and the grain load per cart (25 hu per cart, 1 qian per li per cart).
   - Total grain to be distributed: 10,000 hu.

2. **Procedure**:
   - Calculate the cost of delivering 1 hu of grain for each county:
     - Transportation cost = (distance × 1 qian per li) ÷ 25 hu per cart.
     - Total cost per hu = transportation cost + base grain cost.
   - Use the total cost per hu to calculate the "weight" (衰) for each county:
     - Weight = households ÷ total cost per hu.
   - Normalize the weights to distribute the total grain proportionally:
     - Total weight = sum of all weights.
     - Grain assigned to each county = (weight ÷ total weight) × total grain.

3. **Output**:
   - Grain assigned to each county.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
counties = [
    {"name": "甲", "households": 20520, "base_cost": Fraction(1, 1) + Fraction(20, 100), "distance": 0},
    {"name": "乙", "households": 12312, "base_cost": Fraction(1, 1) + Fraction(10, 100), "distance": 200},
    {"name": "丙", "households": 7182, "base_cost": Fraction(1, 1) + Fraction(12, 100), "distance": 150},
    {"name": "丁", "households": 13338, "base_cost": Fraction(1, 1) + Fraction(17, 100), "distance": 250},
    {"name": "戊", "households": 5130, "base_cost": Fraction(1, 1) + Fraction(13, 100), "distance": 150},
]

total_grain = 10000  # Total grain to be distributed (in hu)
cart_capacity = 25  # Cart capacity (in hu)
transport_cost_per_li = Fraction(1, 100)  # Cost per li per cart

# Step 1: Calculate the total cost per hu for each county
for county in counties:
    transport_cost = (county["distance"] * transport_cost_per_li) / cart_capacity
    county["total_cost_per_hu"] = county["base_cost"] + transport_cost

# Step 2: Calculate the weight (衰) for each county
total_weight = 0
for county in counties:
    county["weight"] = county["households"] / county["total_cost_per_hu"]
    total_weight += county["weight"]

# Step 3: Distribute the grain proportionally based on weights
for county in counties:
    county["grain"] = (county["weight"] / total_weight) * total_grain

# Output the results
for county in counties:
    print(f"{county['name']}縣: {county['grain']}斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**:
   - Each county's data includes the number of households, base grain cost, and distance to the delivery location.
   - Grain transportation cost is calculated based on the distance and cart capacity.

2. **Cost Calculation**:
   - For each county, the total cost per hu is the sum of the base grain cost and the transportation cost.

3. **Weight Calculation**:
   - The weight for each county is calculated as the number of households divided by the total cost per hu.

4. **Grain Distribution**:
   - The total weight is used to normalize the weights, and the grain is distributed proportionally.

5. **Output**:
   - The grain assigned to each county is printed.

---

### Example Output:
The output will show the grain assigned to each county (in hu), ensuring equalized labor and expense. For example:

```
甲縣: a斛
乙縣: b斛
丙縣: c斛
丁縣: d斛
戊縣: e斛
```

Where `a`, `b`, `c`, `d`, and `e` are the calculated grain amounts for each county.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
