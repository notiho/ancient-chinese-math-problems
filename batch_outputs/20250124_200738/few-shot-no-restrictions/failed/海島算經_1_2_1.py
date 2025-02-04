"""
今有南望方邑，不知大小。立兩表東、西去六丈，齊人目，以索連之。令東表與邑東南隅及東北隅參相直。當東表之北卻行五步，遙望邑西北隅，入索東端二丈二尺六寸半。又卻北行去表一十三步二尺，遙望邑西北隅，適與西表相參合。問邑方及邑去表各幾何？
術曰：以入索乘後去表，以兩表相去除之，所得為景差；以前去表減之，不盡以為法。置後去表，以前去表減之，餘以乘入索為實。實如法而一，得邑方。求去表遠近者：置後去表，以景差減之，餘以乘前去表為實。實如法而一，得邑去表。
答曰：邑方 a里 ；邑去表 b里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. The problem involves determining the size of a square city (邑方) and its distance from a reference point (邑去表) based on observations and measurements using poles and ropes. Let's translate the procedure into Python code.

---

### Problem Breakdown:
1. **Given Measurements:**
   - Distance between two poles (兩表相去): 6 丈.
   - Distance north of the eastern pole for the first observation (前去表): 5 步.
   - Rope deviation for the first observation (入索): 2 丈 2 尺 6 寸 5 分 (converted to a single unit).
   - Distance north of the eastern pole for the second observation (後去表): 13 步 2 尺.
   - The second observation aligns with the western pole.

2. **Procedure:**
   - Calculate the difference in shadow lengths (景差).
   - Use the shadow difference and the measurements to calculate the size of the square city (邑方).
   - Use the shadow difference and measurements to calculate the distance of the city from the poles (邑去表).

3. **Units:**
   - 1 丈 = 10 尺.
   - 1 尺 = 10 寸.
   - 1 寸 = 10 分.
   - 1 里 = 300 步.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to a consistent unit (e.g., 尺)
# Given measurements
兩表相去 = 6 * 10  # 6 丈 = 60 尺
前去表 = 5 * 10  # 5 步 = 50 尺
入索 = 2 * 10 + 2 + Fraction(6, 10) + Fraction(5, 100)  # 2 丈 2 尺 6 寸 5 分
後去表 = 13 * 10 + 2  # 13 步 2 尺 = 132 尺

# Step 1: Calculate 景差
景差 = (入索 * 後去表) / 兩表相去

# Step 2: Calculate 邑方 (size of the square city)
法 = 景差 - 前去表
實 = (後去表 - 前去表) * 入索
邑方 = 實 / 法

# Step 3: Calculate 邑去表 (distance of the city from the poles)
法_去表 = 景差
實_去表 = (後去表 - 景差) * 前去表
邑去表 = 實_去表 / 法_去表

# Convert results to 里 (1 里 = 300 步 = 3000 尺)
邑方_里 = 邑方 / 3000
邑去表_里 = 邑去表 / 3000

# Output results
a = 邑方_里
b = 邑去表_里

print(f"邑方: {a} 里")
print(f"邑去表: {b} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion:**
   - All measurements are converted to 尺 for consistency.
   - The final results are converted to 里 (1 里 = 300 步 = 3000 尺).

2. **景差 Calculation:**
   - 景差 is calculated using the formula: `(入索 * 後去表) / 兩表相去`.

3. **邑方 Calculation:**
   - The formula for 邑方 is derived from the problem: `邑方 = 實 / 法`, where:
     - `法 = 景差 - 前去表`.
     - `實 = (後去表 - 前去表) * 入索`.

4. **邑去表 Calculation:**
   - The formula for 邑去表 is: `邑去表 = 實_去表 / 法_去表`, where:
     - `法_去表 = 景差`.
     - `實_去表 = (後去表 - 景差) * 前去表`.

5. **Final Conversion:**
   - Both results are converted to 里 for the final answer.

---

### Example Output:
If you run the code with the given inputs, it will calculate:
- The size of the square city (邑方) in 里.
- The distance of the city from the poles (邑去表) in 里.


"""


"""
Variable 'a' has wrong value. Expected: 151/48, Actual: -6191/1700
Variable 'b' has wrong value. Expected: 83/20, Actual: 83/3020"""
