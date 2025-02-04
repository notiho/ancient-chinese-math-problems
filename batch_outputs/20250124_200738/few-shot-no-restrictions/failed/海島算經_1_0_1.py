"""
今有望海島，立兩表，齊高三丈，前後相去千步，令後表與前表參相直。從前表卻行一百二十三步，人目著地取望島峯，與表末參合。從後表卻行一百二十七步，人目著地取望島峯，亦與表末參合。問島高及去表各幾何？
術曰：以表高乘表間為實；相多為法，除之。所得加表高，即得島高。求前表去島遠近者：以前表卻行乘表間為實；相多為法。除之，得島去表數。
答曰：島高 a里 ；去表 b里 。
"""

"""
This problem involves determining the height of an island and its distance from a reference point using geometric principles and proportional reasoning. Let's translate the ancient Chinese math problem into Python code.

---

### Problem Breakdown:
- Two poles (or markers) are erected, both of equal height (3 zhang).
- The distance between the two poles is 1000 bu.
- Observations are made by walking backward from each pole:
  - From the front pole, walk back 123 bu and observe the island peak aligning with the top of the pole.
  - From the rear pole, walk back 127 bu and observe the same alignment.
- The goal is to calculate:
  1. The height of the island.
  2. The distance from the front pole to the island.

---

### Procedure:
1. **Island Height Calculation**:
   - Multiply the height of the pole by the distance between the poles to get the numerator (實).
   - Subtract the backward walking distances (127 - 123) to get the denominator (法).
   - Divide the numerator by the denominator and add the pole height to get the island height.

2. **Distance to the Island**:
   - Multiply the backward walking distance from the front pole (123 bu) by the distance between the poles to get the numerator (實).
   - Use the same denominator (法) as above.
   - Divide the numerator by the denominator to get the distance from the front pole to the island.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
表高 = 3  # zhang
表間 = 1000  # bu
前表卻行 = 123  # bu
後表卻行 = 127  # bu

# Step 1: Calculate the island height
相多 = 後表卻行 - 前表卻行  # 相多為法
實_島高 = 表高 * 表間  # 表高乘表間為實
島高 = Fraction(實_島高, 相多) + 表高  # 所得加表高，即得島高

# Step 2: Calculate the distance from the front pole to the island
實_去表 = 前表卻行 * 表間  # 前表卻行乘表間為實
去表 = Fraction(實_去表, 相多)  # 除以相多為法，得島去表數

# Convert results to li (1 zhang = 10 bu, 1 li = 300 bu)
島高_里 = Fraction(島高 * 10, 300)  # Convert zhang to bu, then to li
去表_里 = Fraction(去表, 300)  # Convert bu to li

# Final answers
a = 島高_里
b = 去表_里

print(f"島高: {a} 里")
print(f"去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of Units:
1. **Zhang to Bu**: 1 zhang = 10 bu.
2. **Bu to Li**: 1 li = 300 bu.

---

### Output:
The code will compute:
- `a`: The height of the island in li.
- `b`: The distance from the front pole to the island in li.
"""


"""
Variable 'a' has wrong value. Expected: 251/60, Actual: 251/10"""
