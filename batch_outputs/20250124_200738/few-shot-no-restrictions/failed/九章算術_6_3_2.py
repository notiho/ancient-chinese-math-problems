"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex problem involving proportional distribution of grain (粟) among six counties, taking into account transportation costs, labor costs, and the varying distances to the delivery location. Let's break it down step by step and encode it in Python.

---

### Problem Breakdown:
1. **Input Data**:
   - Each county has a certain number of "算" (a unit of labor or tax contribution).
   - Grain prices per dou (斛) vary by county.
   - Labor costs per day vary by county.
   - Distance to the delivery location varies by county.
   - A cart can carry 25 dou of grain, travels 50 li per day when loaded, and 70 li per day when empty. Loading/unloading takes 1 day.

2. **Objective**:
   - Distribute the total grain (60,000 dou) among the six counties such that the labor costs are proportional to their respective "算" values.

3. **Procedure**:
   - Calculate the transportation cost for each county based on distance, cart capacity, and labor costs.
   - Add the cost of grain for each county.
   - Normalize the costs to ensure proportional distribution based on "算".

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Input data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 10, "距離": 0},    # 甲縣 (self-delivery)
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "距離": 70},   # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "距離": 140},   # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "距離": 175},   # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "距離": 210},   # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "距離": 280},   # 己縣
]

# Constants
total_grain = 60000  # Total grain to be distributed (in dou)
cart_capacity = 25   # Cart capacity (in dou)
loaded_speed = 50    # Loaded cart speed (li/day)
empty_speed = 70     # Empty cart speed (li/day)
loading_time = 1     # Loading/unloading time (in days)

# Step 1: Calculate transportation cost per dou for each county
for county in counties:
    if county["距離"] == 0:  # Self-delivery (甲縣)
        county["運費"] = 0
    else:
        # Calculate round-trip time
        distance = county["距離"]
        loaded_time = distance / loaded_speed
        empty_time = distance / empty_speed
        total_time = loaded_time + empty_time + loading_time  # Add loading/unloading time

        # Calculate cost per dou
        labor_cost = total_time * county["傭價"] * 6  # 6 people per cart
        transport_cost_per_dou = labor_cost / cart_capacity
        county["運費"] = transport_cost_per_dou

# Step 2: Calculate total cost per dou (grain price + transport cost)
for county in counties:
    county["總費"] = county["粟價"] + county["運費"]

# Step 3: Normalize costs based on 算 values
# Calculate the divisor (sum of 算 / cost per dou for each county)
divisor = sum(Fraction(county["算"], county["總費"]) for county in counties)

# Step 4: Calculate grain allocation for each county
for county in counties:
    county["分配"] = Fraction(total_grain) * Fraction(county["算"], county["總費"]) / divisor

# Step 5: Output results
results = {county["name"]: county["分配"] for county in counties}

# Print results
for county, grain in results.items():
    print(f"{county}縣: {grain}斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Transportation Cost Calculation**:
   - For each county, calculate the round-trip time for a cart (loaded and empty).
   - Multiply the time by the labor cost per day and divide by the cart capacity to get the cost per dou.

2. **Total Cost per Dou**:
   - Add the grain price per dou to the transportation cost per dou.

3. **Normalization**:
   - Use the formula provided in the problem to normalize the costs based on the "算" values for each county.

4. **Grain Allocation**:
   - Distribute the total grain (60,000 dou) proportionally based on the normalized costs.

5. **Output**:
   - Print the grain allocation for each county.

---

### Example Output:
Assuming the calculations are correct, the output will look something like this:

```
甲縣: a斛
乙縣: b斛
丙縣: c斛
丁縣: d斛
戊縣: e斛
己縣: f斛
```

Where `a`, `b`, `c`, `d`, `e`, and `f` are the allocated grain amounts for each county.
"""


"""
Code error: both arguments should be Rational instances"""
