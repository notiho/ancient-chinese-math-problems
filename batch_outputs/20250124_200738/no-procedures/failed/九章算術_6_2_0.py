"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a classic problem of balancing labor and cost for grain transportation among multiple counties. The goal is to distribute the grain contribution from each county such that the total cost (including transportation and grain value) is equalized across all counties.

Let's break this down step by step and solve it in Python.

---

### Problem Breakdown:
1. Each county has:
   - Number of households.
   - Grain value per hu (斛).
   - Distance to the delivery location.
2. Transportation cost:
   - 1 cart carries 25 hu.
   - Cost per li (里) is 1 qian (錢).
3. Total grain to be delivered: 10,000 hu.
4. The goal is to determine how much grain each county contributes (`a`, `b`, `c`, `d`, `e`) such that the labor and cost are balanced.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# County data: (households, grain value per hu, distance to delivery location)
counties = [
    (20520, Fraction(1, 1) + Fraction(20, 100), 200),  # 甲縣
    (12312, Fraction(1, 1) + Fraction(10, 100), 200),  # 乙縣
    (7182, Fraction(1, 1) + Fraction(12, 100), 150),   # 丙縣
    (13338, Fraction(1, 1) + Fraction(17, 100), 250),  # 丁縣
    (5130, Fraction(1, 1) + Fraction(13, 100), 150)    # 戊縣
]

# Total grain to be delivered
total_grain = 10000

# Transportation cost per hu per li
transport_cost_per_hu_per_li = Fraction(1, 25)

# Calculate the "cost factor" for each county
# Cost factor = (grain value per hu) + (distance * transport cost per hu per li)
cost_factors = []
for households, grain_value, distance in counties:
    transport_cost = distance * transport_cost_per_hu_per_li
    cost_factor = grain_value + transport_cost
    cost_factors.append(cost_factor)

# Total households across all counties
total_households = sum(county[0] for county in counties)

# Calculate the grain contribution for each county
# Grain contribution = (households / total households) * (1 / cost factor)
grain_contributions = []
for i, (households, _, _) in enumerate(counties):
    proportion = Fraction(households, total_households)
    contribution = proportion / cost_factors[i]
    grain_contributions.append(contribution)

# Normalize the contributions so that the total grain equals 10,000 hu
total_contribution = sum(grain_contributions)
normalized_contributions = [contribution * total_grain / total_contribution for contribution in grain_contributions]

# Extract the results
a, b, c, d, e = normalized_contributions

# Print the results
print(f"甲縣: {a} 斛")
print(f"乙縣: {b} 斛")
print(f"丙縣: {c} 斛")
print(f"丁縣: {d} 斛")
print(f"戊縣: {e} 斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Cost Factor Calculation**:
   - For each county, the cost factor is calculated as the sum of the grain value per hu and the transportation cost per hu (based on distance and cart capacity).
2. **Proportional Contribution**:
   - Each county's contribution is proportional to its number of households, adjusted by the inverse of its cost factor (to balance labor and cost).
3. **Normalization**:
   - The contributions are normalized so that the total grain equals 10,000 hu.
4. **Output**:
   - The grain contributions for each county are printed.

---

This approach ensures that the grain contributions are distributed fairly, balancing the cost and labor across all counties.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 56088814600000/16359894697
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 34023105120000/16359894697
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 25366008850000/16359894697
Variable 'd' has wrong value. Expected: 380000/221, Actual: 30027852400000/16359894697
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 18093166000000/16359894697"""
