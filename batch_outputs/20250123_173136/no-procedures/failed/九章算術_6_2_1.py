"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a classic ancient Chinese problem involving proportional distribution based on labor and transportation costs. The goal is to distribute the total amount of grain to be transported among the five counties such that the labor and transportation costs are equalized.

---

### Problem Breakdown:
1. **Given Data**:
   - Total grain to be transported: 10,000 hu.
   - Each cart carries 25 hu, and the cost of transportation is 1 qian per li (mile) per cart.
   - Each county has a specific number of households, grain tax per household, and distance to the delivery location.

   | County | Households | Grain Tax (per household) | Distance (li) |
   |--------|------------|---------------------------|---------------|
   | 甲 (A) | 20,520     | 1 hu 20 qian             | 0             |
   | 乙 (B) | 12,312     | 1 hu 10 qian             | 200           |
   | 丙 (C) | 7,182      | 1 hu 12 qian             | 150           |
   | 丁 (D) | 13,338     | 1 hu 17 qian             | 250           |
   | 戊 (E) | 5,130      | 1 hu 13 qian             | 150           |

2. **Objective**:
   Distribute the total grain (10,000 hu) among the counties such that the labor and transportation costs are equalized.

3. **Key Formula**:
   The cost for each county is proportional to:
   \[
   \text{Cost} = \text{Grain Amount} \times \left( \text{Distance Cost per hu} + \text{Grain Tax per hu} \right)
   \]
   Where:
   - Distance Cost per hu = \(\frac{\text{Distance (li)}}{25}\) (since 1 cart carries 25 hu).
   - Grain Tax per hu is given for each county.

4. **Solution**:
   Let \(a, b, c, d, e\) represent the grain amounts allocated to counties A, B, C, D, and E, respectively. The total grain is distributed such that:
   \[
   a + b + c + d + e = 10,000
   \]
   And the costs for all counties are equalized.

---

### Python Code Solution:


"""


from fractions import Fraction

# County data
counties = [
    {"households": 20520, "grain_tax": Fraction(120, 100), "distance": 0},     # County A
    {"households": 12312, "grain_tax": Fraction(110, 100), "distance": 200},   # County B
    {"households": 7182,  "grain_tax": Fraction(112, 100), "distance": 150},   # County C
    {"households": 13338, "grain_tax": Fraction(117, 100), "distance": 250},   # County D
    {"households": 5130,  "grain_tax": Fraction(113, 100), "distance": 150},   # County E
]

# Total grain to be distributed
total_grain = 10000

# Transportation cost per hu for each county
for county in counties:
    distance_cost = Fraction(county["distance"], 25)  # Cost per hu based on distance
    county["total_cost_per_hu"] = county["grain_tax"] + distance_cost

# Calculate the inverse of total cost per hu for proportional distribution
total_inverse_cost = sum(Fraction(1, county["total_cost_per_hu"]) for county in counties)

# Allocate grain to each county
for county in counties:
    county["grain_allocation"] = Fraction(1, county["total_cost_per_hu"]) / total_inverse_cost * total_grain

# Extract results
a = counties[0]["grain_allocation"]
b = counties[1]["grain_allocation"]
c = counties[2]["grain_allocation"]
d = counties[3]["grain_allocation"]
e = counties[4]["grain_allocation"]

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
   - Each county's household count, grain tax, and distance are stored in a dictionary.
   - The grain tax is converted into a `Fraction` to ensure precise calculations.

2. **Cost Calculation**:
   - For each county, the total cost per hu is calculated as the sum of the grain tax and the transportation cost.

3. **Proportional Distribution**:
   - The grain is distributed inversely proportional to the total cost per hu for each county.
   - The inverse of the total cost per hu is summed up for all counties, and each county's share is calculated as a fraction of this total.

4. **Output**:
   - The grain allocation for each county is printed as a fraction for precision.

---

### Example Output:
```
甲縣得 2345/2 斛
乙縣得 1234/3 斛
丙縣得 4567/4 斛
丁縣得 5678/5 斛
戊縣得 6789/6 斛
```

(Note: The actual output will depend on the precise calculations, which are handled exactly using fractions.)
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 16125534197500/2541611593
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 2126444070000/2541611593
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 2717786662500/2541611593
Variable 'd' has wrong value. Expected: 380000/221, Actual: 1732376100000/2541611593
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 2713974900000/2541611593"""
