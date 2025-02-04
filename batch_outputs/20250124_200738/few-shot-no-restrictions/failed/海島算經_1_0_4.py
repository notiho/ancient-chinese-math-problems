"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving similar triangles. The problem describes a method to calculate the height of an island and its distance from a reference point using two poles of equal height and observations from specific distances. Let's translate this into Python code.

---

### Problem Breakdown:
1. **Given:**
   - Two poles of equal height: 3 zhang (丈).
   - Distance between the two poles: 1000 bu (步).
   - Observations:
     - From the front pole, walking back 123 bu aligns the top of the pole with the peak of the island.
     - From the rear pole, walking back 127 bu aligns the top of the pole with the peak of the island.

2. **To Find:**
   - The height of the island (`島高`).
   - The distance from the front pole to the island (`去表`).

3. **Procedure:**
   - Use the height of the pole and the distances to form similar triangles.
   - Calculate the height of the island using the formula:
     \[
     島高 = 表高 + \frac{{表高 \times 表間}}{{相多}}
     \]
   - Calculate the distance from the front pole to the island using:
     \[
     去表 = \frac{{前表卻行 \times 表間}}{{相多}}
     \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
表高 = 3  # Pole height in 丈
表間 = 1000  # Distance between the two poles in 步
前表卻行 = 123  # Distance walked back from the front pole in 步
後表卻行 = 127  # Distance walked back from the rear pole in 步

# 相多 = 後表卻行 - 前表卻行
相多 = 後表卻行 - 前表卻行

# Calculate 島高 (height of the island)
島高 = 表高 + Fraction(表高 * 表間, 相多)

# Calculate 去表 (distance from the front pole to the island)
去表 = Fraction(前表卻行 * 表間, 相多)

# Convert results to 丈 (1 丈 = 10 步)
島高_in_里 = 島高 / 10
去表_in_里 = 去表 / 10

# Output results
a = 島高_in_里
b = 去表_in_里

print(f"島高: {a} 里")
print(f"去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data:**
   - The height of the poles (`表高`), the distance between the poles (`表間`), and the distances walked back from the poles (`前表卻行`, `後表卻行`).

2. **Key Calculations:**
   - `相多` is the difference between the distances walked back from the rear and front poles.
   - The height of the island (`島高`) is calculated using the formula provided in the problem.
   - The distance from the front pole to the island (`去表`) is calculated similarly.

3. **Unit Conversion:**
   - Since the problem asks for the results in `里`, and 1 丈 = 10 步, we divide the results by 10.

4. **Output:**
   - The height of the island (`島高`) and the distance to the island (`去表`) are printed in `里`.

---

### Example Output:
If you run the code, it will calculate the height of the island and its distance from the front pole in `里`. The use of `Fraction` ensures precise calculations, as ancient Chinese mathematics often involved rational numbers.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 753/10
Variable 'b' has wrong value. Expected: 205/2, Actual: 3075"""
