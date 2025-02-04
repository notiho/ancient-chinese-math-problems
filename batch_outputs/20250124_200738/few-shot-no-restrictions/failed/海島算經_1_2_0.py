"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. The problem involves determining the size of a square city (邑方) and its distance from a reference point (邑去表) based on observations and measurements using poles and strings. Let's translate this into Python code step by step.

---

### Problem Breakdown:
1. **Given Measurements:**
   - Distance between the two poles (東表 and 西表): `6 丈`
   - First observation:
     - Distance north of the east pole: `5 步`
     - String deviation (入索): `2 丈 2 尺 6 寸半`
   - Second observation:
     - Distance north of the east pole: `13 步 2 尺`
     - String deviation aligns with the west pole.

2. **Goal:**
   - Determine the size of the square city (邑方, `a`).
   - Determine the distance from the poles to the city (邑去表, `b`).

3. **Procedure:**
   - Calculate the difference in shadow lengths (景差) using the formula:
     \[
     景差 = \frac{\text{入索} \times \text{後去表}}{\text{兩表相去}}
     \]
   - Use 景差 to calculate the size of the city (邑方):
     \[
     邑方 = \frac{\text{入索} \times (\text{後去表} - \text{前去表})}{\text{景差}}
     \]
   - Use 景差 to calculate the distance to the city (邑去表):
     \[
     邑去表 = \frac{\text{前去表} \times (\text{後去表} - \text{景差})}{\text{景差}}
     \]

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to a consistent base (e.g., 丈)
# 1 丈 = 10 尺, 1 尺 = 10 寸
def to_zhang(zhang=0, chi=0, cun=0):
    return zhang + Fraction(chi, 10) + Fraction(cun, 100)

# Given data
兩表相去 = to_zhang(zhang=6)  # Distance between the two poles
前去表 = to_zhang(chi=5)  # First observation distance north of the east pole
入索 = to_zhang(zhang=2, chi=2, cun=6.5)  # String deviation in the first observation
後去表 = to_zhang(chi=13, cun=2)  # Second observation distance north of the east pole

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 邑方 (size of the city)
邑方 = (入索 * (後去表 - 前去表)) / 景差

# Step 3: Calculate 邑去表 (distance to the city)
邑去表 = (前去表 * (後去表 - 景差)) / 景差

# Convert results to 里 (1 里 = 300 丈)
邑方_in_li = 邑方 / 300
邑去表_in_li = 邑去表 / 300

# Output results
a = 邑方_in_li
b = 邑去表_in_li

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:** The function `to_zhang` converts measurements in 丈, 尺, and 寸 into a single unit (丈) for consistent calculations.
2. **景差 Calculation:** The difference in shadow lengths is calculated using the formula provided in the problem.
3. **邑方 Calculation:** The size of the square city is determined using the formula involving 景差 and 入索.
4. **邑去表 Calculation:** The distance from the poles to the city is calculated using 景差 and the distances north of the poles.
5. **Conversion to 里:** Since the final answer is required in 里, the results are divided by 300 (1 里 = 300 丈).

---

### Example Output:
If you run the code with the given data, it will compute the size of the city (邑方) and its distance from the poles (邑去表) in 里. The exact values will depend on the calculations based on the provided measurements.
"""


"""
Code error: both arguments should be Rational instances"""
