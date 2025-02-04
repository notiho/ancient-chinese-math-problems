"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning to calculate the width of a river mouth (波口廣). Let's translate the problem and solution into Python code.

### Problem Breakdown:
1. Two poles (表) are placed 9 丈 apart (南北相去九丈).
2. Observations are made from different positions west of the northern pole:
   - At 6 丈 west of the northern pole, the observer sees the southern bank of the river mouth (波口南岸) entering the rope (索) at 4 丈 2 寸 from the northern end.
   - The observer also sees the northern bank entering the rope 1 丈 2 尺 inside the northern pole.
   - At 13 丈 5 尺 west of the northern pole, the observer sees the southern bank aligning with the southern pole.

3. The goal is to calculate the width of the river mouth (波口廣).

### Procedure:
1. Multiply the distance of the second observation point (13 丈 5 尺) from the northern pole by the distance the rope enters at the first observation (4 丈 2 寸).
2. Subtract the distance of the first observation point (6 丈) from the northern pole from the result.
3. Use the difference as the divisor (法).
4. Subtract the first observation point's distance from the second observation point's distance, and multiply the result by the distance the rope enters at the northern pole (1 丈 2 尺).
5. Divide the result by the divisor to get the width of the river mouth.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Convert units to consistent fractions of 丈
def convert_to_zhang(zhang, chi=0, cun=0):
    return Fraction(zhang) + Fraction(chi, 10) + Fraction(cun, 100)

# Given data
表相去 = convert_to_zhang(9)  # Distance between the two poles (9 丈)
前去表 = convert_to_zhang(6)  # Distance of the first observation point from the northern pole (6 丈)
後去表 = convert_to_zhang(13, 5)  # Distance of the second observation point from the northern pole (13 丈 5 尺)
入索 = convert_to_zhang(4, 2)  # Distance the rope enters at the first observation (4 丈 2 寸)
入表里 = convert_to_zhang(1, 2)  # Distance the rope enters at the northern pole (1 丈 2 尺)

# Step 1: Multiply the second observation distance by the rope entry distance
step1 = 後去表 * 入索

# Step 2: Subtract the first observation distance
法 = step1 - 前去表

# Step 3: Subtract the first observation distance from the second observation distance
step3 = 後去表 - 前去表

# Step 4: Multiply the result by the rope entry distance at the northern pole
實 = step3 * 入表里

# Step 5: Divide the result by the divisor to get the width of the river mouth
波口廣 = 實 / 法

# Convert the result to 丈
a = 波口廣

# Output the result
print(f"波口廣: {float(a):.2f} 丈 ({a} as a fraction)")
#----- content ends here -----


"""


---

### Explanation of Units:
- 1 丈 = 10 尺
- 1 尺 = 10 寸
- All calculations are converted to fractions of 丈 for consistency.

### Example Output:
If you run the code, it will calculate the width of the river mouth (波口廣) in 丈. The result will be displayed both as a decimal and as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 30/169"""
