"""
今有東南望波口，立兩表南、北相去九丈，以索薄地連之。當北表之西卻行去表六丈，薄地遙望波口南岸，入索北端四丈二寸。以望北岸，入前所望表里一丈二尺。又卻後行去表一十三丈五尺。薄地遙望波口南岸，與南表參合。問波口廣幾何？
術曰：以後去表乘入索，如表相去而一。所得，以前去表減之，餘以為法；復以前去表減後去表，餘以乘入所望表里為實，實如法而一，得波口廣。
答曰： a里 。
"""

"""
This is a classic ancient Chinese surveying problem involving geometry and proportional reasoning. Let's translate the problem and solution into Python code.

### Problem Breakdown:
1. Two poles (north and south) are placed 9 zhang apart.
2. Measurements are taken by moving westward from the north pole and observing the wave mouth (波口) from different positions:
   - At 6 zhang west of the north pole, the rope (索) enters the north end by 4 zhang 2 cun (4.2 zhang).
   - Observing the north bank, the rope enters the pole by 1 zhang 2 chi (1.2 zhang).
   - Moving further west, 13 zhang 5 chi (13.5 zhang) from the north pole, the rope aligns with the south pole.

### Procedure:
1. Multiply the second westward distance (13.5 zhang) by the rope's entry at the north end (4.2 zhang).
2. Subtract the first westward distance (6 zhang) from the pole separation (9 zhang) to get the divisor.
3. Subtract the first westward distance (6 zhang) from the second westward distance (13.5 zhang).
4. Multiply the result by the rope's entry at the north bank (1.2 zhang) to get the dividend.
5. Divide the dividend by the divisor to get the width of the wave mouth.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
表相去 = 9  # Distance between the poles (in zhang)
前去表 = 6  # First westward distance from the north pole (in zhang)
入索 = Fraction(42, 10)  # Rope entry at the north end (4 zhang 2 cun = 4.2 zhang)
入表里 = Fraction(12, 10)  # Rope entry at the north bank (1 zhang 2 chi = 1.2 zhang)
後去表 = Fraction(135, 10)  # Second westward distance from the north pole (13 zhang 5 chi = 13.5 zhang)

# Step 1: Multiply the second westward distance by the rope entry at the north end
step1 = 後去表 * 入索

# Step 2: Subtract the first westward distance from the pole separation to get the divisor
法 = 表相去 - 前去表

# Step 3: Subtract the first westward distance from the second westward distance
step3 = 後去表 - 前去表

# Step 4: Multiply the result by the rope entry at the north bank to get the dividend
實 = step3 * 入表里

# Step 5: Divide the dividend by the divisor to get the width of the wave mouth
波口廣 = Fraction(實, 法)

# Convert to li (1 zhang = 1/300 li)
波口廣_里 = 波口廣 / 300

# Output the result
a = 波口廣_里
print(f"波口廣: {a} 里")
#----- content ends here -----


"""


### Explanation of Units:
- 1 zhang = 10 chi.
- 1 li = 300 zhang.

### Example Output:
If you run the code, it will calculate the width of the wave mouth in li (`a`).
"""


"""
Variable 'a' has wrong value. Expected: 5/3, Actual: 1/100"""
