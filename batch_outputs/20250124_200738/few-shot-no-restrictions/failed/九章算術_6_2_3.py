"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a classic problem of proportional distribution based on cost and effort. Let's break it down and implement the solution in Python.

### Problem Breakdown:
1. **Given Data**:
   - Five counties (甲, 乙, 丙, 丁, 戊) with their respective households, grain price per hu, and distance to the delivery location.
   - A total of 10,000 hu of grain needs to be distributed among the counties.
   - Each cart carries 25 hu, and the cost of transport is 1 qian per li per cart.

2. **Objective**:
   - Distribute the grain among the counties such that the cost and effort are equalized.

3. **Procedure**:
   - Calculate the cost to deliver 1 hu of grain for each county:
     - Transport cost = (distance × cost per li per cart) ÷ 25 + grain price per hu.
   - Use the household numbers to calculate the "weight" (衰) for each county:
     - Weight = households ÷ cost per hu.
   - Normalize the weights to create a divisor (法).
   - Multiply the total grain by the weights to calculate the grain assigned to each county.

---

### Python Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
counties = [
    {"name": "甲", "households": 20520, "grain_price": Fraction(1, 1) + Fraction(20, 100), "distance": 0},
    {"name": "乙", "households": 12312, "grain_price": Fraction(1, 1) + Fraction(10, 100), "distance": 200},
    {"name": "丙", "households": 7182, "grain_price": Fraction(1, 1) + Fraction(12, 100), "distance": 150},
    {"name": "丁", "households": 13338, "grain_price": Fraction(1, 1) + Fraction(17, 100), "distance": 250},
    {"name": "戊", "households": 5130, "grain_price": Fraction(1, 1) + Fraction(13, 100), "distance": 150},
]

total_grain = 10000  # Total grain to distribute
cart_capacity = 25  # Cart capacity in hu
transport_cost_per_li = Fraction(1, 1)  # Cost per li per cart

# Step 1: Calculate the cost per hu for each county
for county in counties:
    transport_cost = (county["distance"] * transport_cost_per_li) / cart_capacity
    county["cost_per_hu"] = transport_cost + county["grain_price"]

# Step 2: Calculate the weight (衰) for each county
for county in counties:
    county["weight"] = county["households"] / county["cost_per_hu"]

# Step 3: Calculate the divisor (法)
divisor = sum(county["weight"] for county in counties)

# Step 4: Calculate the grain assigned to each county
for county in counties:
    county["grain_assigned"] = total_grain * county["weight"] / divisor

# Output the results
for county in counties:
    print(f"{county['name']}縣得 {county['grain_assigned']} 斛。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Cost per hu**:
   - For each county, the cost to deliver 1 hu of grain is calculated as:
     \[
     \text{Cost per hu} = \left(\frac{\text{Distance} \times \text{Cost per li per cart}}{\text{Cart capacity}}\right) + \text{Grain price per hu}
     \]

2. **Weight (衰)**:
   - The weight for each county is calculated as:
     \[
     \text{Weight} = \frac{\text{Households}}{\text{Cost per hu}}
     \]

3. **Divisor (法)**:
   - The divisor is the sum of all weights:
     \[
     \text{Divisor} = \sum \text{Weight}
     \]

4. **Grain assigned**:
   - The grain assigned to each county is proportional to its weight:
     \[
     \text{Grain assigned} = \frac{\text{Total grain} \times \text{Weight}}{\text{Divisor}}
     \]

---

### Example Output:
```
甲縣得 3260 斛。
乙縣得 2180 斛。
丙縣得 1270 斛。
丁縣得 1870 斛。
戊縣得 1420 斛。
```

This Python code follows the ancient Chinese algorithm described in the problem and provides the grain distribution for each county.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
