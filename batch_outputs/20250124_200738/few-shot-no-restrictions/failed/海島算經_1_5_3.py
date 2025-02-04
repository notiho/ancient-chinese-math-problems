"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. Let's break it down and translate it into Python code step by step.

---

### Problem Description:
We are tasked with calculating the width of a river mouth (波口廣). The problem involves two observation points and measurements using poles and ropes. The steps to solve the problem are described in the procedure.

---

### Procedure:
1. Multiply the distance from the second observation point to the pole (後去表) by the rope's offset (入索).
2. Divide the result by the distance between the poles (表相去).
3. Subtract the distance from the first observation point to the pole (前去表) from the result to get the divisor (法).
4. Subtract the first observation point's distance to the pole (前去表) from the second observation point's distance to the pole (後去表).
5. Multiply the result by the rope's offset at the first observation point (入所望表里) to get the dividend (實).
6. Divide the dividend by the divisor to get the width of the river mouth.

---

### Given Data:
- Distance between the poles (表相去): 9 丈
- Distance from the second observation point to the pole (後去表): 13 丈 5 尺
- Distance from the first observation point to the pole (前去表): 6 丈
- Rope's offset at the second observation point (入索): 4 丈 2 寸
- Rope's offset at the first observation point (入所望表里): 1 丈 2 尺

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert all measurements to a consistent unit (e.g., 尺)
# 1 丈 = 10 尺, 1 尺 = 10 寸

# Given data
表相去 = 9 * 10  # 9 丈 = 90 尺
後去表 = 13 * 10 + 5  # 13 丈 5 尺 = 135 尺
前去表 = 6 * 10  # 6 丈 = 60 尺
入索 = 4 * 10 + 2 / 10  # 4 丈 2 寸 = 40 尺 + 0.2 尺 = 40.2 尺
入所望表里 = 1 * 10 + 2  # 1 丈 2 尺 = 12 尺

# Step 1: Multiply 後去表 by 入索
step1 = 後去表 * 入索

# Step 2: Divide by 表相去
step2 = Fraction(step1, 表相去)

# Step 3: Subtract 前去表 to get the divisor (法)
法 = step2 - 前去表

# Step 4: Subtract 前去表 from 後去表
step4 = 後去表 - 前去表

# Step 5: Multiply the result by 入所望表里 to get the dividend (實)
實 = step4 * 入所望表里

# Step 6: Divide the dividend by the divisor to get the width of the river mouth
波口廣 = Fraction(實, 法)

# Convert the result to 丈 for the final answer
波口廣_in_丈 = 波口廣 / 10

# Output the result
a = 波口廣_in_丈
print(f"波口廣: {a} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Unit Conversion**: All measurements are converted to 尺 for consistency.
2. **Step-by-Step Calculation**: Each step of the procedure is implemented in Python, following the ancient algorithm.
3. **Fraction Handling**: The `Fraction` class is used to ensure precise calculations, especially since the problem involves divisions.
4. **Final Conversion**: The result is converted back to 丈 for the final answer.

---

### Final Answer:
The width of the river mouth (波口廣) is `a` 丈.
"""


"""
Code error: both arguments should be Rational instances"""
