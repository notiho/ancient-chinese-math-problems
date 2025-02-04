"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This is a classic problem of proportional distribution based on weights (衰) derived from distances and other factors. Let's translate the problem into Python code step by step.

---

### Problem Breakdown:
- There are 5 counties (甲, 乙, 丙, 丁, 戊) with different populations and distances (measured in days of travel).
- The total number of laborers required for one month is 1200.
- The labor distribution is proportional to the "weights" (衰) of each county, which are determined by their population and travel days.

---

### Procedure:
1. **Determine the weights (衰):**
   - Multiply the population of each county by the travel days + 1 (居所及行道日數而一).
   - These weights are used to calculate the proportional contribution of each county.

2. **Sum the weights (副并為法):**
   - Add all the weights together to get the divisor (法).

3. **Calculate the contribution (實如法而一):**
   - Multiply the total labor requirement (1200) by the weight of each county and divide by the total weight.

4. **Handle fractional results:**
   - If there are fractional results, adjust them by distributing the remainder proportionally.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# County data: (population, travel days)
counties = {
    "甲": (1200, 3),  # 3 days + 1 = 4
    "乙": (1550, 4),  # 4 days + 1 = 5
    "丙": (1280, 3),  # 3 days + 1 = 4
    "丁": (990, 2),   # 2 days + 1 = 3
    "戊": (1750, 4),  # 4 days + 1 = 5
}

# Total labor requirement
total_labor = 1200

# Step 1: Calculate weights (衰)
weights = {county: population * (days + 1) for county, (population, days) in counties.items()}

# Step 2: Sum the weights (副并為法)
total_weight = sum(weights.values())

# Step 3: Calculate contributions (實如法而一)
contributions = {county: Fraction(weight * total_labor, total_weight) for county, weight in weights.items()}

# Step 4: Handle fractional results (分者，上下輩之)
# Convert contributions to integers, distributing any remainder
integer_contributions = {county: int(contribution) for county, contribution in contributions.items()}
remainder = total_labor - sum(integer_contributions.values())

# Distribute the remainder proportionally
if remainder > 0:
    sorted_counties = sorted(contributions.items(), key=lambda x: x[1] - int(x[1]), reverse=True)
    for i in range(remainder):
        county = sorted_counties[i][0]
        integer_contributions[county] += 1

# Final results
a = integer_contributions["甲"]
b = integer_contributions["乙"]
c = integer_contributions["丙"]
d = integer_contributions["丁"]
e = integer_contributions["戊"]

# Output results
print(f"甲縣 {a}人")
print(f"乙縣 {b}人")
print(f"丙縣 {c}人")
print(f"丁縣 {d}人")
print(f"戊縣 {e}人")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Weights Calculation:**
   - Each county's weight is calculated as `population * (travel days + 1)`.

2. **Proportional Distribution:**
   - The total labor (1200) is distributed proportionally to the weights.

3. **Handling Fractions:**
   - Since laborers must be whole numbers, any remainder is distributed to the counties with the largest fractional parts.

4. **Output:**
   - The final number of laborers assigned to each county is printed.

---

### Example Output:
If you run the code, you'll get the number of laborers assigned to each county (甲, 乙, 丙, 丁, 戊) based on the given data.
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 196
Variable 'b' has wrong value. Expected: 286, Actual: 317
Variable 'c' has wrong value. Expected: 228, Actual: 209
Variable 'd' has wrong value. Expected: 171, Actual: 121
Variable 'e' has wrong value. Expected: 286, Actual: 357"""
