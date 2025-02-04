"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing the labor force (輸卒) among five counties (甲, 乙, 丙, 丁, 戊) based on their population and distance traveled, while ensuring fairness according to the principle of proportionality. Here's how we solve it step by step:

---

### Problem Breakdown:
1. **Given Data**:
   - 甲縣: 1200 people, distance = 0 days (薄塞, meaning no travel).
   - 乙縣: 1550 people, distance = 1 day.
   - 丙縣: 1280 people, distance = 2 days.
   - 丁縣: 990 people, distance = 3 days.
   - 戊縣: 1750 people, distance = 5 days.
   - Total labor required for one month: 1200 people.

2. **Principle**:
   - The labor distribution is proportional to both the population of the county and the distance traveled. Counties farther away contribute less labor per capita.

3. **Objective**:
   - Calculate the number of people (a, b, c, d, e) each county contributes to the total labor force of 1200 people.

---

### Solution:

We calculate the contribution of each county using the formula:

\[
\text{Contribution Factor} = \frac{\text{Population}}{\text{Distance + 1}}
\]

The "+1" in the denominator ensures that counties with zero travel distance (like 甲縣) are still included in the calculation.

---

### Python Code:


"""


from fractions import Fraction

# Given data
populations = [1200, 1550, 1280, 990, 1750]  # Population of each county
distances = [0, 1, 2, 3, 5]  # Distance in days for each county
total_labor = 1200  # Total labor required for one month

# Calculate contribution factors for each county
contribution_factors = [Fraction(populations[i], distances[i] + 1) for i in range(5)]

# Calculate the total contribution factor
total_contribution_factor = sum(contribution_factors)

# Calculate the labor assigned to each county
labor_distribution = [Fraction(total_labor) * factor / total_contribution_factor for factor in contribution_factors]

# Extract results
a, b, c, d, e = labor_distribution

# Print results
print(f"甲縣: {a} 人")
print(f"乙縣: {b} 人")
print(f"丙縣: {c} 人")
print(f"丁縣: {d} 人")
print(f"戊縣: {e} 人")


"""


---

### Explanation of the Code:
1. **Contribution Factor**:
   - Each county's contribution factor is calculated as the population divided by (distance + 1).
   - This ensures that counties farther away contribute less labor.

2. **Total Contribution Factor**:
   - The sum of all contribution factors is used to normalize the labor distribution.

3. **Labor Distribution**:
   - Each county's labor contribution is proportional to its contribution factor relative to the total contribution factor.

4. **Fraction**:
   - The `Fraction` class is used to ensure exact calculations without floating-point errors.

---

### Output:
The output will provide the labor distribution for each county in terms of exact fractions or simplified integers, depending on the input values.
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 1728000/3529
Variable 'b' has wrong value. Expected: 286, Actual: 1116000/3529
Variable 'c' has wrong value. Expected: 228, Actual: 614400/3529
Variable 'd' has wrong value. Expected: 171, Actual: 356400/3529
Variable 'e' has wrong value. Expected: 286, Actual: 420000/3529"""
