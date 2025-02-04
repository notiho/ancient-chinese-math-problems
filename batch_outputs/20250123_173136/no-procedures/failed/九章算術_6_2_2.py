"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a classic problem of proportional allocation based on labor and transportation costs. The goal is to distribute the total amount of grain to be transported (10,000 hu) among the five counties such that the labor cost (including transportation distance and rental costs) is equalized.

Let's break this down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Data**:
   - Each county has a certain number of households, a base grain tax rate (in hu and qian), and a distance to the delivery location.
   - Transportation cost: 1 qian per li per cartload (25 hu per cart).
   - Total grain to be transported: 10,000 hu.

2. **Objective**:
   - Distribute the grain among the counties such that the total labor cost (grain tax + transportation cost) is equalized.

3. **Approach**:
   - Calculate the labor cost per hu for each county, which includes:
     - Grain tax per hu.
     - Transportation cost per hu (based on distance and cart capacity).
   - Use the labor cost per hu as weights to proportionally allocate the total grain (10,000 hu) among the counties.

---

### Python Code:


"""


from fractions import Fraction

# Data for each county
counties = [
    {"households": 20520, "grain_tax": Fraction(1, 1) + Fraction(20, 100), "distance": 200},
    {"households": 12312, "grain_tax": Fraction(1, 1) + Fraction(10, 100), "distance": 200},
    {"households": 7182, "grain_tax": Fraction(1, 1) + Fraction(12, 100), "distance": 150},
    {"households": 13338, "grain_tax": Fraction(1, 1) + Fraction(17, 100), "distance": 250},
    {"households": 5130, "grain_tax": Fraction(1, 1) + Fraction(13, 100), "distance": 150},
]

# Transportation cost per hu (1 cart = 25 hu, 1 qian per li per cart)
cart_capacity = 25
transport_cost_per_hu = lambda distance: Fraction(distance, cart_capacity)

# Calculate labor cost per hu for each county
for county in counties:
    county["labor_cost_per_hu"] = county["grain_tax"] + transport_cost_per_hu(county["distance"])

# Calculate the total labor cost weight
total_weight = sum(county["households"] * county["labor_cost_per_hu"] for county in counties)

# Allocate the total grain (10,000 hu) proportionally based on labor cost weights
total_grain = 10000
for county in counties:
    county["allocated_grain"] = total_grain * (county["households"] * county["labor_cost_per_hu"]) / total_weight

# Extract results
a, b, c, d, e = [county["allocated_grain"] for county in counties]

# Print results
print(f"甲縣得 {a} 斛")
print(f"乙縣得 {b} 斛")
print(f"丙縣得 {c} 斛")
print(f"丁縣得 {d} 斛")
print(f"戊縣得 {e} 斛")


"""


---

### Explanation of the Code:
1. **Input Data**:
   - Each county's data includes the number of households, grain tax per hu, and distance to the delivery location.
   - Grain tax is converted into a `Fraction` to handle precision.

2. **Labor Cost Calculation**:
   - The labor cost per hu is the sum of the grain tax and the transportation cost per hu (calculated based on distance and cart capacity).

3. **Proportional Allocation**:
   - The total labor cost weight is calculated as the sum of `(households * labor_cost_per_hu)` for all counties.
   - Grain is allocated proportionally based on each county's contribution to the total labor cost weight.

4. **Output**:
   - The grain allocated to each county is stored in `a`, `b`, `c`, `d`, and `e`.

---

### Example Output:
The output will provide the amount of grain (in hu) allocated to each county such that the labor cost is equalized. The results will be in fractions for precise representation.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 18400000/5239
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 840000/403
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 4984000/5239
Variable 'd' has wrong value. Expected: 380000/221, Actual: 1117000/403
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 115000/169"""
