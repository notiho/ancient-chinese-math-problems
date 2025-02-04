"""
今有均輸粟：甲縣一萬戶，行道八日；乙縣九千五百戶，行道十日；丙縣一萬二千三百五十戶，行道十三日；丁縣一萬二千二百戶，行道二十日，各到輸所。凡四縣賦，當輸二十五萬斛，用車一萬乘。欲以道里遠近，戶數多少，衰出之。問︰粟、車各幾何？
均輸術曰：令縣戶數，各如其本行道日數而一，以為衰。甲衰一百二十五，乙、丙衰各九十五，丁衰六十一，副并為法。以賦粟、車數乘未并者，各自為實。實如法得一車。有分者，上下輩之。以二十五斛乘車數，即粟數。
荅曰：甲縣粟 a斛 ，車 b乘 。乙縣粟 c斛 ，車 d乘 。丙縣粟 e斛 ，車 f乘 。丁縣粟 g斛 ，車 h乘 。
"""

"""
This problem involves distributing grain and carts among four counties based on their population and distance to the delivery location. The solution uses proportional allocation based on the given rules.

### Problem Breakdown:
- **Counties**: Four counties (甲, 乙, 丙, 丁) with respective populations and travel days.
- **Total Grain**: 250,000 hu.
- **Total Carts**: 10,000 carts.
- **Proportional Allocation**: Based on the product of the population and travel days for each county.

### Procedure:
1. **Calculate the "weight" (衰)** for each county:
   - Multiply the population of each county by its travel days.
2. **Sum the weights** to get the divisor (法).
3. **Calculate the "real" values (實)**:
   - Multiply the total grain and total carts by each county's weight.
4. **Divide the real values by the divisor** to get the allocation for each county.
5. **Adjust for fractional values**:
   - Grain and carts are rounded appropriately.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# County data: (population, travel days)
counties = {
    "甲": (10000, 8),
    "乙": (9500, 10),
    "丙": (12350, 13),
    "丁": (12200, 20),
}

# Total grain and carts
total_grain = 250000  # hu
total_carts = 10000   # carts

# Step 1: Calculate weights (衰)
weights = {county: population * days for county, (population, days) in counties.items()}

# Step 2: Calculate the divisor (法)
divisor = sum(weights.values())

# Step 3: Calculate real values (實) for grain and carts
grain_allocation = {county: Fraction(weight * total_grain, divisor) for county, weight in weights.items()}
cart_allocation = {county: Fraction(weight * total_carts, divisor) for county, weight in weights.items()}

# Step 4: Convert to integers (rounding appropriately)
grain_allocation_rounded = {county: round(value) for county, value in grain_allocation.items()}
cart_allocation_rounded = {county: round(value) for county, value in cart_allocation.items()}

# Results
for county in counties:
    print(f"{county}縣粟 {grain_allocation_rounded[county]}斛 ，車 {cart_allocation_rounded[county]}乘 。")
#----- content ends here -----


"""


### Explanation of Code:
1. **Weights Calculation**:
   - Each county's weight is calculated as `population * travel_days`.
2. **Divisor (法)**:
   - The sum of all weights is used as the divisor for proportional allocation.
3. **Real Values (實)**:
   - The total grain and carts are multiplied by each county's weight and divided by the divisor.
4. **Rounding**:
   - Since grain and carts must be integers, the results are rounded appropriately.

### Output:
The program will output the grain and cart allocation for each county in the format:
```
甲縣粟 a斛 ，車 b乘 。
乙縣粟 c斛 ，車 d乘 。
丙縣粟 e斛 ，車 f乘 。
丁縣粟 g斛 ，車 h乘 。
```
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'"""
