"""
今有均賦粟：甲縣二萬五百二十戶，粟一斛二十錢，自輸其縣；乙縣一萬二千三百一十二戶，粟一斛一十錢，至輸所二百里；丙縣七千一百八十二戶，粟一斛一十二錢，至輸所一百五十里；丁縣一萬三千三百三十八戶，粟一斛一十七錢，至輸所二百五十里；戊縣五千一百三十戶，粟一斛一十三錢，至輸所一百五十里。凡五縣賦，輸粟一萬斛。一車載二十五斛，與僦一里一錢。欲以縣戶輸粟，令費勞等。問︰縣各粟幾何？
荅曰：甲縣 a斛 。乙縣 b斛 。丙縣 c斛 。丁縣 d斛 。戊縣 e斛 。
"""

"""
This is a classic problem of balancing labor and cost in transporting grain from multiple counties to a central location. The goal is to distribute the total grain (10,000 hu) among the counties such that the labor cost (transportation cost) is equalized across all counties.

### Problem Breakdown:
1. Each county has a specific number of households, a grain tax rate (in hu and qian), and a distance to the central location.
2. Transportation cost is calculated based on the distance and the amount of grain transported. Each cart carries 25 hu, and the cost is 1 qian per li per cart.
3. The task is to determine how much grain each county should contribute such that the transportation cost per household is equal across all counties.

---

### Variables:
- **Households (戶)**: Number of households in each county.
- **Grain tax rate (粟)**: Amount of grain (in hu and qian) each household contributes.
- **Distance (里)**: Distance from the county to the central location.
- **Total grain (輸粟)**: 10,000 hu to be distributed among the counties.
- **Cart capacity**: 25 hu per cart.
- **Transportation cost**: 1 qian per li per cart.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# County data: (households, grain tax rate in qian, distance in li)
counties = [
    (20520, Fraction(120, 100), 200),  # 甲縣: 20520戶, 1斛20錢, 200里
    (12312, Fraction(110, 100), 200),  # 乙縣: 12312戶, 1斛10錢, 200里
    (7182, Fraction(112, 100), 150),   # 丙縣: 7182戶, 1斛12錢, 150里
    (13338, Fraction(117, 100), 250),  # 丁縣: 13338戶, 1斛17錢, 250里
    (5130, Fraction(113, 100), 150),   # 戊縣: 5130戶, 1斛13錢, 150里
]

# Total grain to be distributed
total_grain = 10000

# Cart capacity and transportation cost per li per cart
cart_capacity = 25
cost_per_li_per_cart = 1

# Calculate the "labor cost factor" for each county
# Labor cost factor = (grain tax rate * distance) / households
labor_cost_factors = []
for households, grain_tax_rate, distance in counties:
    labor_cost_factor = (grain_tax_rate * distance) / households
    labor_cost_factors.append(labor_cost_factor)

# Find the total inverse of labor cost factors (to normalize contributions)
total_inverse_factor = sum(1 / factor for factor in labor_cost_factors)

# Calculate the grain contribution for each county
grain_contributions = []
for factor in labor_cost_factors:
    contribution = total_grain / (factor * total_inverse_factor)
    grain_contributions.append(contribution)

# Output the results
a, b, c, d, e = [Fraction(contribution).limit_denominator() for contribution in grain_contributions]
print(f"甲縣: {a}斛")
print(f"乙縣: {b}斛")
print(f"丙縣: {c}斛")
print(f"丁縣: {d}斛")
print(f"戊縣: {e}斛")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Labor Cost Factor**: This is calculated as `(grain tax rate * distance) / households`. It represents the relative labor cost for each county.
2. **Normalization**: The total inverse of the labor cost factors is used to normalize the contributions, ensuring that the labor cost per household is equal across all counties.
3. **Grain Contribution**: Each county's contribution is proportional to the inverse of its labor cost factor, normalized by the total grain to be distributed.

---

### Output:
The output will provide the grain contribution for each county (甲縣, 乙縣, 丙縣, 丁縣, 戊縣) in hu, ensuring that the transportation cost per household is equalized.
"""


"""
Variable 'a' has wrong value. Expected: 10260000/2873, Actual: 372900000/113431
Variable 'b' has wrong value. Expected: 6840000/2873, Actual: 244080000/113431
Variable 'c' has wrong value. Expected: 3990000/2873, Actual: 186450000/113431
Variable 'd' has wrong value. Expected: 380000/221, Actual: 198880000/113431
Variable 'e' has wrong value. Expected: 2700000/2873, Actual: 132000000/113431"""
