"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. Let's break it down and translate it into Python code.

### Problem Breakdown:
1. Two poles (表) are placed 9 丈 apart, one to the south and one to the north.
2. Observations are made from different positions west of the northern pole:
   - At 6 丈 west of the northern pole, the line of sight to the southern bank of the river enters the northern end of the rope by 4 丈 2 寸.
   - The line of sight to the northern bank enters the pole by 1 丈 2 尺.
   - At 13 丈 5 尺 west of the northern pole, the line of sight to the southern bank aligns with the southern pole.
3. The goal is to calculate the width of the river (波口廣).

### Procedure:
1. Multiply the distance of the second observation point from the northern pole (13 丈 5 尺) by the amount the rope enters the northern end (4 丈 2 寸).
2. Subtract the distance of the first observation point (6 丈) from the result.
3. Use the difference as the divisor (法).
4. Subtract the first observation point (6 丈) from the second observation point (13 丈 5 尺).
5. Multiply the result by the amount the line of sight enters the northern pole (1 丈 2 尺).
6. Divide the product by the divisor to get the width of the river.

### Units Conversion:
- 1 丈 = 10 尺
- 1 尺 = 10 寸

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert measurements to 尺 for consistency
丈_to_尺 = 10
尺_to_寸 = 10

# Given data
表相去 = 9 * 丈_to_尺  # Distance between the two poles (9 丈)
前去表 = 6 * 丈_to_尺  # Distance of the first observation point (6 丈)
入索 = 4 * 丈_to_尺 + 2  # Rope enters northern end (4 丈 2 寸)
入表里 = 1 * 丈_to_尺 + 2  # Line of sight enters northern pole (1 丈 2 尺)
後去表 = 13 * 丈_to_尺 + 5  # Distance of the second observation point (13 丈 5 尺)

# Step 1: Multiply the second observation distance by the rope entry
step1 = 後去表 * 入索

# Step 2: Subtract the first observation distance
法 = step1 - 前去表

# Step 3: Subtract the first observation distance from the second observation distance
step3 = 後去表 - 前去表

# Step 4: Multiply the result by the line of sight entry
實 = step3 * 入表里

# Step 5: Divide the product by the divisor to get the width of the river
波口廣 = Fraction(實, 法)

# Convert the result to 丈 for the final answer
波口廣_in_丈 = 波口廣 / 丈_to_尺

# Output the result
a = 波口廣_in_丈
print(f"波口廣: {a} 丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. All measurements are converted to 尺 for consistency.
2. The procedure is implemented step by step as described in the problem.
3. The final result is converted back to 丈 for the answer.

### Example Output:
If you run the code, the result will be the width of the river (波口廣) in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 3/187"""
