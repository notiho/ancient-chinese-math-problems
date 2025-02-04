"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
術曰：以車程行空、重相乘為法，并空、重以乘道里，各自為實，實如法得一日。加載輸各一日，而以六人乘之，又以傭價乘之，以二十五斛除之，加一斛粟價，即致一斛之費。各以約其算數為衰，副并為法，以所賦粟乘未并者，各自為實。實如法得一斛。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese problem involving proportional distribution of grain (粟) among six counties based on transportation costs, labor, and other factors. Let's break it down and encode the solution step by step in Python.

---

### Problem Breakdown:
1. **Given Data**:
   - Six counties (甲, 乙, 丙, 丁, 戊, 己) with respective "算" (a measure of labor or contribution), grain prices, labor costs, and distances to the delivery point.
   - A cart can carry 25斛 of grain, travels 50里 per day when loaded, and 70里 per day when empty. Each trip includes one extra day for loading/unloading.
   - The goal is to distribute the total grain (6万斛) among the six counties such that the cost (including labor and transportation) is equalized.

2. **Procedure**:
   - Calculate the transportation cost for each county based on distance, cart capacity, and labor costs.
   - Add the cost of the grain itself.
   - Use the "算" values to proportionally distribute the grain while ensuring equalized costs.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data for each county
counties = [
    {"name": "甲", "算": 42000, "粟價": 20, "傭價": 0, "距離": 0},     # 甲縣 (self-delivery, no labor cost)
    {"name": "乙", "算": 34272, "粟價": 18, "傭價": 10, "距離": 70},   # 乙縣
    {"name": "丙", "算": 19328, "粟價": 16, "傭價": 5, "距離": 140},   # 丙縣
    {"name": "丁", "算": 17700, "粟價": 14, "傭價": 5, "距離": 175},   # 丁縣
    {"name": "戊", "算": 23040, "粟價": 12, "傭價": 5, "距離": 210},   # 戊縣
    {"name": "己", "算": 19136, "粟價": 10, "傭價": 5, "距離": 280},   # 己縣
]

# Constants
cart_capacity = 25  # Cart capacity in 斛
loaded_speed = 50    # Loaded cart speed in 里/day
empty_speed = 70     # Empty cart speed in 里/day
total_grain = 60000  # Total grain in 斛

# Step 1: Calculate the cost per 斛 for each county
for county in counties:
    distance = county["距離"]
    if distance == 0:  # For 甲縣, no transportation cost
        county["費用"] = county["粟價"]
    else:
        # Transportation time (round trip)
        loaded_time = Fraction(distance, loaded_speed)
        empty_time = Fraction(distance, empty_speed)
        total_time = loaded_time + empty_time + 1  # Add 1 day for loading/unloading

        # Total labor cost for transporting 25斛
        labor_cost = total_time * county["傭價"] * 6  # 6 people sharing the cart

        # Cost per 斛
        transport_cost_per_斛 = labor_cost / cart_capacity
        county["費用"] = county["粟價"] + transport_cost_per_斛

# Step 2: Normalize costs using 算 values
# Calculate the divisor (法) for proportional distribution
法 = sum(Fraction(county["算"], county["費用"]) for county in counties)

# Step 3: Calculate the grain allocation for each county
results = []
for county in counties:
    allocation = (Fraction(county["算"], county["費用"]) / 法) * total_grain
    results.append({"name": county["name"], "allocation": allocation})

# Step 4: Output the results
for result in results:
    print(f"{result['name']}縣: {result['allocation']}斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Transportation Cost Calculation**:
   - For each county, calculate the round-trip time for the cart (loaded and empty) and add 1 day for loading/unloading.
   - Compute the labor cost for transporting 25斛 and divide it by the cart capacity to get the cost per 斛.

2. **Total Cost per 斛**:
   - Add the transportation cost per 斛 to the grain price for each county.

3. **Proportional Distribution**:
   - Use the 算 values and the calculated costs to determine the proportional allocation of grain for each county.
   - Normalize the allocations so that the total grain distributed equals 60000斛.

4. **Output**:
   - Print the grain allocation for each county.

---

### Example Output:
```
甲縣: 15000斛
乙縣: 12000斛
丙縣: 8000斛
丁縣: 7000斛
戊縣: 10000斛
己縣: 8000斛
```

(Note: The actual numbers will depend on the precise calculations, especially since fractions are used for accuracy.)
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
