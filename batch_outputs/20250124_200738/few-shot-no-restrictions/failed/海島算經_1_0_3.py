"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
This is a classic surveying problem from ancient Chinese mathematics, involving the use of similar triangles to calculate the height of an island and its distance from a reference point. Let us solve it step by step using Python.

### Problem Breakdown:
1. Two poles (or markers) of equal height (3 zhang) are placed 1000 bu apart.
2. Observations are made from two positions:
   - From the first pole, walking back 123 bu, the top of the island aligns with the top of the pole.
   - From the second pole, walking back 127 bu, the top of the island aligns with the top of the pole.
3. Using these observations, calculate:
   - The height of the island.
   - The distance from the first pole to the island.

### Procedure:
1. Use the formula for similar triangles:
   - Island height = (Pole height × Distance between poles) ÷ Difference in backward steps.
   - Add the pole height to get the total island height.
2. To calculate the distance from the first pole to the island:
   - Distance = (Backward steps from the first pole × Distance between poles) ÷ Difference in backward steps.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
表高 = 3  # Height of the poles in zhang
表間 = 1000  # Distance between the two poles in bu
前表卻行 = 123  # Steps backward from the first pole in bu
後表卻行 = 127  # Steps backward from the second pole in bu

# Step 1: Calculate the difference in backward steps
相多 = 後表卻行 - 前表卻行  # Difference in backward steps

# Step 2: Calculate the height of the island
島高 = Fraction(表高 * 表間, 相多) + 表高  # Add the pole height to the result

# Step 3: Calculate the distance from the first pole to the island
島去表 = Fraction(前表卻行 * 表間, 相多)

# Convert results to li (1 li = 300 bu)
島高_里 = Fraction(島高, 300)
島去表_里 = Fraction(島去表, 300)

# Final results
a = 島高_里  # Height of the island in li
b = 島去表_里  # Distance from the first pole to the island in li

# Print results
print(f"島高: {a} 里")
print(f"去表: {b} 里")
#----- content ends here -----


"""


### Explanation of the Code:
1. **表高**: The height of the poles is given as 3 zhang.
2. **表間**: The distance between the two poles is 1000 bu.
3. **前表卻行** and **後表卻行**: The backward steps from the first and second poles are 123 bu and 127 bu, respectively.
4. **相多**: The difference in backward steps is calculated as `後表卻行 - 前表卻行`.
5. **島高**: The height of the island is calculated using the formula `(Pole height × Distance between poles) ÷ Difference in backward steps`, and the pole height is added to the result.
6. **島去表**: The distance from the first pole to the island is calculated using the formula `(Backward steps from the first pole × Distance between poles) ÷ Difference in backward steps`.
7. **Conversion to li**: Since 1 li = 300 bu, the results are converted to li for the final answer.

### Final Answer:
- 島高: `a` 里 (height of the island in li)
- 去表: `b` 里 (distance from the first pole to the island in li)
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/100"""
