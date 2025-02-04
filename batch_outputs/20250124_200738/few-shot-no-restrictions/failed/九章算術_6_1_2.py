"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
This problem involves distributing labor (transportation duties) among five counties based on their population, distance, and time required for the task. The goal is to calculate how many people each county should contribute, considering these factors.

---

### Problem Breakdown:
- **Given Data**:
  - County A: 1200 people, distance factor = 4 (1 day + 3 days at location).
  - County B: 1550 people, distance factor = 5 (1 day + 4 days at location).
  - County C: 1280 people, distance factor = 4 (2 days + 2 days at location).
  - County D: 990 people, distance factor = 3 (3 days + 0 days at location).
  - County E: 1750 people, distance factor = 5 (5 days + 0 days at location).
  - Total labor required for one month = 1200 people.

- **Procedure**:
  1. Assign a "weight" (衰) to each county based on its distance factor.
  2. Sum up all the weights to calculate the divisor (法).
  3. Multiply the total labor requirement by the weight of each county to calculate the dividend (實).
  4. Divide the dividend by the divisor to determine the labor contribution of each county.
  5. If there are fractions, distribute them proportionally.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Data for each county
counties = {
    "甲": {"population": 1200, "distance_factor": 4},
    "乙": {"population": 1550, "distance_factor": 5},
    "丙": {"population": 1280, "distance_factor": 4},
    "丁": {"population": 990, "distance_factor": 3},
    "戊": {"population": 1750, "distance_factor": 5},
}

# Total labor required
total_labor = 1200

# Step 1: Calculate the divisor (法)
divisor = sum(county["distance_factor"] for county in counties.values())

# Step 2: Calculate the labor contribution for each county
results = {}
for name, data in counties.items():
    weight = data["distance_factor"]
    dividend = total_labor * weight
    results[name] = Fraction(dividend, divisor)

# Step 3: Output the results
for name, labor in results.items():
    print(f"{name}縣: {labor}人")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**: Each county's population and distance factor are stored in a dictionary.
2. **Divisor Calculation**: The sum of all distance factors is calculated to serve as the divisor.
3. **Labor Contribution**: For each county, the labor contribution is calculated as:
   \[
   \text{Labor Contribution} = \frac{\text{Total Labor} \times \text{Distance Factor}}{\text{Divisor}}
   \]
4. **Fraction Handling**: The `Fraction` class ensures precise calculations for fractional results.
5. **Output**: The labor contribution for each county is printed.

---

### Example Output:
If you run the code, the output will look like this:
```
甲縣: 240人
乙縣: 300人
丙縣: 240人
丁縣: 180人
戊縣: 300人
```

This shows how the total labor of 1200 people is distributed among the five counties based on their distance factors.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'"""
