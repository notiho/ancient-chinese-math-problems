"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
術曰：以一里僦價，乘至輸所里，以一車二十五斛除之，加一斛粟價，則致一斛之費。各以約其戶數，為衰。甲衰一千二十六，乙衰六百八十四，丙衰三百九十九，丁衰四百九十四，戊衰二百七十，副并為法。所賦粟乘未并者，各自為實。實如法得一。
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a complex problem involving proportional distribution of grain (粟) among five counties based on their respective transportation costs and household counts, ensuring equal labor and cost burdens. Let's break it down step by step and encode the solution in Python.

---

### Problem Breakdown:
1. **Given Data**:
   - Each county has a number of households, a base grain price per hu (斛), and a distance to the delivery location.
   - Transportation cost is calculated as 1 qian (錢) per li (里) per cart, where each cart carries 25 hu.
   - The total grain to be distributed is 10,000 hu.

2. **Procedure**:
   - Calculate the cost to deliver 1 hu of grain for each county:
     - Transportation cost = `(distance × 1 qian) / 25 hu per cart`.
     - Total cost per hu = transportation cost + base grain price per hu.
   - Use the household count of each county to calculate its "weight" (衰).
     - Weight = `household count / cost per hu`.
   - Normalize the weights to find the proportion of grain each county should deliver.
   - Distribute the total grain (10,000 hu) proportionally based on the weights.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# County data: (households, base grain price per hu, distance to delivery location)
counties = {
    "甲": {"households": 20520, "grain_price": Fraction(1, 1) + Fraction(20, 100), "distance": 0},
    "乙": {"households": 12312, "grain_price": Fraction(1, 1) + Fraction(10, 100), "distance": 200},
    "丙": {"households": 7182, "grain_price": Fraction(1, 1) + Fraction(12, 100), "distance": 150},
    "丁": {"households": 13338, "grain_price": Fraction(1, 1) + Fraction(17, 100), "distance": 250},
    "戊": {"households": 5130, "grain_price": Fraction(1, 1) + Fraction(13, 100), "distance": 150},
}

# Constants
grain_total = 10000  # Total grain to be distributed (in hu)
cart_capacity = 25   # Each cart carries 25 hu
transport_cost_per_li = 1  # Cost per li per cart (in qian)

# Step 1: Calculate the cost to deliver 1 hu of grain for each county
for county, data in counties.items():
    transport_cost = (data["distance"] * transport_cost_per_li) / cart_capacity
    total_cost_per_hu = data["grain_price"] + transport_cost
    data["total_cost_per_hu"] = total_cost_per_hu

# Step 2: Calculate the weight (衰) for each county
total_weight = 0
for county, data in counties.items():
    weight = data["households"] / data["total_cost_per_hu"]
    data["weight"] = weight
    total_weight += weight

# Step 3: Distribute the total grain proportionally based on weights
for county, data in counties.items():
    grain_share = grain_total * (data["weight"] / total_weight)
    data["grain_share"] = grain_share

# Step 4: Output the results
for county, data in counties.items():
    print(f"{county}縣: {data['grain_share']}斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**:
   - Each county's household count, grain price per hu, and distance to the delivery location are stored in a dictionary.

2. **Cost Calculation**:
   - For each county, the total cost to deliver 1 hu of grain is calculated by adding the transportation cost to the base grain price.

3. **Weight Calculation**:
   - The weight (衰) for each county is calculated as the ratio of household count to the total cost per hu.

4. **Grain Distribution**:
   - The total grain (10,000 hu) is distributed proportionally based on the weights.

5. **Output**:
   - The grain share for each county is printed.

---

### Example Output:
Assuming the calculations are correct, the output will look something like this:

```
甲縣: a斛
乙縣: b斛
丙縣: c斛
丁縣: d斛
戊縣: e斛
```

Where `a`, `b`, `c`, `d`, and `e` are the respective grain shares for each county.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
