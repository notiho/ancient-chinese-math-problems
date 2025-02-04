"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. Let's break it down and translate it into Python code step by step.

---

### Problem Breakdown:
1. **Setup**:
   - Two poles (南表 and 北表) are placed 9 丈 apart (南北相去九丈).
   - A rope is stretched across the ground (索薄地連之).
   - Observations are made from different positions to determine the width of the river mouth (波口廣).

2. **Observations**:
   - From a position 6 丈 west of the 北表, the rope enters the northern end of the pole by 4 丈 2 寸 (入索北端四丈二寸).
   - From the same position, when looking at the northern bank, the rope enters the pole by 1 丈 2 尺 (入前所望表里一丈二尺).
   - Moving further back to a position 13 丈 5 尺 west of the 北表, the rope aligns with the 南表 when looking at the southern bank.

3. **Goal**:
   - Calculate the width of the river mouth (波口廣).

4. **Procedure**:
   - Multiply the distance from the second observation point to the 北表 (後去表) by the rope's entry point at the northern end (入索).
   - Subtract the first observation point's distance to the 北表 (前去表) from the result.
   - Use the difference as the divisor (法).
   - Subtract the first observation point's distance to the 北表 (前去表) from the second observation point's distance to the 北表 (後去表).
   - Multiply the result by the rope's entry point at the northern bank (入所望表里).
   - Divide the product by the divisor to get the width of the river mouth.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
南北相去 = 9  # Distance between 南表 and 北表 in 丈
前去表 = 6  # Distance from the first observation point to 北表 in 丈
後去表 = Fraction(135, 10)  # Distance from the second observation point to 北表 in 丈 (13 丈 5 尺 = 13.5 丈)
入索 = Fraction(42, 10)  # Rope entry at the northern end in 丈 (4 丈 2 寸 = 4.2 丈)
入所望表里 = Fraction(12, 10)  # Rope entry at the northern bank in 丈 (1 丈 2 尺 = 1.2 丈)

# Step 1: Calculate the divisor (法)
法 = 後去表 * 入索 - 前去表 * 入索

# Step 2: Calculate the numerator (實)
實 = (後去表 - 前去表) * 入所望表里

# Step 3: Calculate the width of the river mouth (波口廣)
波口廣 = 實 / 法

# Convert to 里 (1 里 = 300 丈)
波口廣_里 = 波口廣 / 300

# Output the result
a = 波口廣_里
print(f"波口廣: {a} 里")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**:
   - All distances are converted into consistent units (丈).
   - Fractions are used to handle non-integer values (e.g., 4 丈 2 寸 = 4.2 丈).

2. **Calculation**:
   - The divisor (法) is calculated using the formula: `(後去表 * 入索) - (前去表 * 入索)`.
   - The numerator (實) is calculated using the formula: `(後去表 - 前去表) * 入所望表里`.
   - The width of the river mouth (波口廣) is obtained by dividing the numerator by the divisor.

3. **Conversion**:
   - The result is converted from 丈 to 里 (1 里 = 300 丈).

---

### Example Output:
If you run the code, it will compute the width of the river mouth in 里. The result will be stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/1050"""
