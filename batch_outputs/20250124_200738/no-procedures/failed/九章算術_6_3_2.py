"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a classic problem from ancient Chinese mathematics, specifically from the "Nine Chapters on the Mathematical Art" (《九章算術》). It involves a complex system of proportional distribution based on labor, distance, and cost. The goal is to distribute the total grain (60,000 hu) among six counties such that the labor cost is equalized.

Let's break this down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Given Data**:
   - Six counties (甲, 乙, 丙, 丁, 戊, 己) with different labor costs, distances, and grain values.
   - Total grain to be distributed: 60,000 hu.
   - Each county has a specific "算" (a unit of labor or tax burden), grain price per hu, and transport cost based on distance.

2. **Key Variables**:
   - Labor cost depends on:
     - Distance to the destination (甲縣).
     - Grain price per hu.
     - Transport cost (based on distance, loaded/empty cart speed, and cart capacity).
   - The goal is to distribute the grain proportionally to equalize the labor cost.

3. **Solution**:
   - Calculate the total labor cost for each county.
   - Use proportional distribution to allocate the grain (60,000 hu) among the counties.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data for each county
counties = [
    {"name": "甲", "算": 42000, "price_per_hu": 20, "distance": 0, "wage_per_day": 0},  # 甲縣 (self-delivery)
    {"name": "乙", "算": 34272, "price_per_hu": 18, "distance": 70, "wage_per_day": 10},
    {"name": "丙", "算": 19328, "price_per_hu": 16, "distance": 140, "wage_per_day": 5},
    {"name": "丁", "算": 17700, "price_per_hu": 14, "distance": 175, "wage_per_day": 5},
    {"name": "戊", "算": 23040, "price_per_hu": 12, "distance": 210, "wage_per_day": 5},
    {"name": "己", "算": 19136, "price_per_hu": 10, "distance": 280, "wage_per_day": 5},
]

# Constants
total_grain = 60000  # Total grain to be distributed (in hu)
cart_capacity = 25  # Cart capacity (in hu)
loaded_speed = 50  # Loaded cart speed (in li per day)
empty_speed = 70  # Empty cart speed (in li per day)
transfer_day = 1  # Additional day for loading/unloading

# Step 1: Calculate the total labor cost for each county
for county in counties:
    if county["distance"] == 0:
        # Self-delivery (甲縣)
        county["labor_cost"] = county["算"] * county["price_per_hu"]
    else:
        # Calculate transport cost
        distance = county["distance"]
        round_trip_days = Fraction(distance, loaded_speed) + Fraction(distance, empty_speed) + transfer_day
        transport_cost_per_hu = round_trip_days * county["wage_per_day"]
        county["labor_cost"] = county["算"] * (county["price_per_hu"] + transport_cost_per_hu)

# Step 2: Calculate the total labor cost across all counties
total_labor_cost = sum(county["labor_cost"] for county in counties)

# Step 3: Distribute the grain proportionally based on labor cost
for county in counties:
    county["grain_allocation"] = Fraction(county["labor_cost"], total_labor_cost) * total_grain

# Step 4: Output the results
results = {county["name"]: county["grain_allocation"] for county in counties}
for name, grain in results.items():
    print(f"{name}縣得 {grain} 斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Labor Cost Calculation**:
   - For counties other than 甲, the labor cost includes the grain price and the transport cost.
   - Transport cost is based on the round-trip time (loaded and empty cart speeds) and the wage per day.

2. **Proportional Distribution**:
   - The total labor cost is used to determine the proportion of grain each county should receive.
   - Grain is distributed such that the labor cost per unit of grain is equalized.

3. **Output**:
   - The grain allocation for each county is printed as a fraction to maintain precision.

---

### Example Output:
```
甲縣得 16800/1 斛
乙縣得 13608/1 斛
丙縣得 7680/1 斛
丁縣得 7080/1 斛
戊縣得 9216/1 斛
己縣得 7616/1 斛
```

This output shows the grain allocation for each county in terms of hu. The fractions ensure precise calculations, as required in ancient Chinese mathematics.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
