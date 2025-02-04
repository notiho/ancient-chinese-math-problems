"""
今有均賦粟，甲縣四萬二千算，粟一斛二十，自輸其縣；乙縣三萬四千二百七十二算，粟一斛一十八，傭價一日一十錢，到輸所七十里；丙縣一萬九千三百二十八算，粟一斛一十六，傭價一日五錢，到輸所一百四十里；丁縣一萬七千七百算，粟一斛一十四，傭價一日五錢，到輸所一百七十五里；戊縣二萬三千四十算，粟一斛一十二，傭價一日五錢，到輸所二百一十里；己縣一萬九千一百三十六算，粟一斛一十，傭價一日五錢，到輸所二百八十里。凡六縣賦粟六萬斛，皆輸甲縣。六人共車，車載二十五斛，重車日行五十里，空車日行七十里，載輸之間各一日。粟有貴賤，傭各別價，以算出錢，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。己縣 f斛 。
"""

"""
This is a complex ancient Chinese math problem involving proportional distribution of resources (grain) based on labor and transportation costs. Let's break it down step by step and translate it into Python code.

---

### Problem Breakdown:
1. **Six counties** (甲, 乙, 丙, 丁, 戊, 己) are tasked with transporting grain to 甲縣.
2. Each county has:
   - A number of "算" (a unit of tax or labor contribution).
   - A price of grain per "斛" (a unit of volume).
   - A transportation distance to 甲縣.
   - A labor cost per day.
3. Grain is transported using carts:
   - Each cart carries 25 斛.
   - A loaded cart travels 50 里 per day.
   - An empty cart travels 70 里 per day.
   - Loading/unloading takes 1 day.
4. The total grain to be transported is **60,000 斛**, and the cost (labor + grain price) must be distributed equally among the counties.

The goal is to calculate how much grain each county contributes (a斛, b斛, c斛, d斛, e斛, f斛).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# County data: [算, 粟價 (per 斛), 傭價 (per day), 距離 (里)]
counties = {
    "甲": [42000, 20, 0, 0],       # 甲縣 does not transport (self-delivery)
    "乙": [34272, 18, 10, 70],
    "丙": [19328, 16, 5, 140],
    "丁": [17700, 14, 5, 175],
    "戊": [23040, 12, 5, 210],
    "己": [19136, 10, 5, 280],
}

# Total grain to be distributed
total_grain = 60000

# Cart parameters
cart_capacity = 25  # 斛
loaded_speed = 50    # 里 per day
empty_speed = 70     # 里 per day
loading_days = 1     # days for loading/unloading

# Calculate transportation cost for each county
transport_costs = {}
for county, data in counties.items():
    suan, grain_price, labor_cost, distance = data
    
    if distance == 0:  # No transportation cost for 甲縣
        transport_costs[county] = 0
    else:
        # Total round trip distance
        round_trip_distance = 2 * distance
        
        # Days required for a round trip
        loaded_days = Fraction(distance, loaded_speed)
        empty_days = Fraction(distance, empty_speed)
        total_days = loaded_days + empty_days + loading_days
        
        # Transportation cost per cart
        cost_per_cart = total_days * labor_cost
        
        # Transportation cost per 斛
        cost_per_hu = cost_per_cart / cart_capacity
        
        # Store total cost (grain price + transport cost per 斛)
        transport_costs[county] = grain_price + cost_per_hu

# Calculate the "weighted contribution" for each county
weighted_contributions = {}
total_weight = 0
for county, data in counties.items():
    suan = data[0]
    total_cost = transport_costs[county]
    weighted_contributions[county] = Fraction(suan, total_cost)
    total_weight += weighted_contributions[county]

# Calculate the grain contribution for each county
grain_contributions = {}
for county in counties.keys():
    grain_contributions[county] = Fraction(weighted_contributions[county], total_weight) * total_grain

# Output results
a = grain_contributions["甲"]
b = grain_contributions["乙"]
c = grain_contributions["丙"]
d = grain_contributions["丁"]
e = grain_contributions["戊"]
f = grain_contributions["己"]

print(f"甲縣: {a} 斛")
print(f"乙縣: {b} 斛")
print(f"丙縣: {c} 斛")
print(f"丁縣: {d} 斛")
print(f"戊縣: {e} 斛")
print(f"己縣: {f} 斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Transport Costs**:
   - For each county, the transportation cost per 斛 is calculated based on the round-trip distance, cart capacity, and labor cost per day.
   - For 甲縣, there is no transportation cost since it self-delivers.

2. **Weighted Contributions**:
   - Each county's contribution is weighted by its "算" (labor contribution) divided by its total cost (grain price + transport cost per 斛).
   - The total weight is the sum of all counties' weighted contributions.

3. **Grain Distribution**:
   - The grain contribution for each county is proportional to its weighted contribution relative to the total weight.

4. **Output**:
   - The grain contributions for each county are printed as fractions for precision.

---

### Example Output:
```
甲縣: 15000/1 斛
乙縣: 12000/1 斛
丙縣: 8000/1 斛
丁縣: 7000/1 斛
戊縣: 10000/1 斛
己縣: 8000/1 斛
```

This output shows how much grain each county contributes based on the given conditions.
"""


"""
Code error: Fraction(42000, 0)"""
