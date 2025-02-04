"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing labor (soldiers) among five counties based on their distance and the number of days required for transportation. Here's the solution translated into Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
# Format: (number of people, travel days)
counties = {
    "甲": (1200, 1),
    "乙": (1550, 1),
    "丙": (1280, 2),
    "丁": (990, 3),
    "戊": (1750, 5),
}

# Total labor to be distributed in one month
total_labor = 1200

# Step 1: Determine the "衰" (weight) for each county
# 衰 = people * (1 + travel days)
weights = {county: people * (1 + days) for county, (people, days) in counties.items()}

# Step 2: Calculate the divisor (法)
法 = sum(weights.values())

# Step 3: Calculate the actual labor distribution
# 实 = total_labor * weight / 法
distribution = {county: Fraction(total_labor * weight, 法) for county, weight in weights.items()}

# Step 4: Output the results
for county, labor in distribution.items():
    print(f"{county}縣: {labor}人")
#----- content ends here -----


"""


### Explanation of the Steps:
1. **Determine the "衰" (weight):**  
   Each county's weight is calculated based on its population and the number of travel days. The formula is:  
   \[
   \text{衰} = \text{people} \times (1 + \text{travel days})
   \]

2. **Calculate the divisor (法):**  
   The divisor is the sum of all weights.

3. **Distribute the labor:**  
   The labor for each county is proportional to its weight. The formula is:  
   \[
   \text{Labor for a county} = \frac{\text{total labor} \times \text{weight of the county}}{\text{divisor}}
   \]

4. **Output the results:**  
   The results are displayed as fractions to ensure precision.

### Example Output:
If you run the code, the output will look something like this (in fractional form):
```
甲縣: a人
乙縣: b人
丙縣: c人
丁縣: d人
戊縣: e人
```

You can replace the fractions with decimal approximations if needed. Let me know if you'd like me to calculate the exact values!
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
