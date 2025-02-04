"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. The problem describes a method to calculate the size of a square city (邑方) and its distance from a reference point (邑去表) using observations and measurements.

Let's translate the problem into Python code step by step.

---

### Problem Breakdown:
1. **Given Measurements:**
   - Distance between the two poles (東表 and 西表): `6 丈`
   - Distance walked north from the east pole for the first observation: `5 步`
   - The rope (索) enters the east pole by `2 丈 2 尺 6 寸 5 分` (convert to a single unit).
   - Distance walked further north for the second observation: `13 步 2 尺`.

2. **Objective:**
   - Calculate the size of the square city (邑方, `a`).
   - Calculate the distance from the poles to the city (邑去表, `b`).

3. **Procedure:**
   - Use the given formulas to calculate the shadow difference (景差) and then the size of the city and its distance.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to a consistent base (e.g., "丈" as the base unit)
# 1 丈 = 10 尺, 1 尺 = 10 寸, 1 寸 = 10 分

# Given data
兩表相去 = 6  # Distance between the two poles in 丈
前去表 = 5  # Distance walked north for the first observation in 步
入索 = 2 + Fraction(2, 10) + Fraction(6, 100) + Fraction(5, 1000)  # Rope enters in 丈 (2丈2尺6寸5分)
後去表 = 13 + Fraction(2, 10)  # Distance walked further north in 步

# Step 1: Calculate 景差 (shadow difference)
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 邑方 (size of the square city)
法 = 後去表 - 前去表 - 景差  # 法 = (後去表 - 前去表 - 景差)
實 = 入索 * (後去表 - 前去表)  # 實 = 入索 * (後去表 - 前去表)
邑方 = 實 / 法  # 邑方 = 實 / 法

# Step 3: Calculate 邑去表 (distance from the poles to the city)
法_去表 = 景差  # 法 for distance calculation
實_去表 = 前去表 * (後去表 - 景差)  # 實 for distance calculation
邑去表 = 實_去表 / 法_去表  # 邑去表 = 實 / 法

# Convert results to 丈 for final answer
a = 邑方  # Size of the square city in 丈
b = 邑去表  # Distance from the poles to the city in 丈

# Output the results
print(f"邑方: {a} 丈")
print(f"邑去表: {b} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:** All measurements are converted to the base unit of 丈 for consistency.
2. **Formulas:**
   - 景差 is calculated using the formula: `(入索 * 後去表) / 兩表相去`.
   - 邑方 is calculated using the formula: `實 / 法`, where `實 = 入索 * (後去表 - 前去表)` and `法 = 後去表 - 前去表 - 景差`.
   - 邑去表 is calculated using the formula: `實 / 法`, where `實 = 前去表 * (後去表 - 景差)` and `法 = 景差`.
3. **Fractions:** The `Fraction` class is used to ensure precise calculations, especially when dealing with non-integer values.

---

### Example Output:
If you run the code with the given data, it will calculate the size of the square city (邑方) and its distance from the poles (邑去表) in 丈. You can further convert the results to other units (e.g., 里) if needed.
"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: 18573/3217
Variable 'b' has wrong value. Expected: 83/20, Actual: 1245/151"""
