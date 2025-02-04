"""
今有塹上廣一丈六尺三寸下廣一丈深六尺三寸袤一十三丈二尺一寸問積幾何
荅曰一萬九百四十三尺八寸
夏程人功八百七十一尺并出土功五分之一沙礫水石之功作太半定功二百三十二尺一十五分尺之四問用徒幾何
術曰置本人功去其出土功五分之一又去沙礫水石之功太半餘為法以塹積尺為實實如法而一即用徒人數
荅曰 a人 
"""

#----- content starts here -----
"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question 1: What is the volume of the trench?
Answer: 10,943 chi 8 cun.

Additionally, the following labor details are provided:
- Standard labor per person: 871 chi
- Earth removal labor: 1/5 of the total labor
- Labor for sand, gravel, water, and stones: more than half (太半) of the total labor
- Final adjusted labor: 232 chi and 4/15 chi

Question 2: How many workers are needed?

The procedure says:
1. Place the standard labor per person.
2. Subtract the earth removal labor (1/5 of the total labor).
3. Subtract the labor for sand, gravel, water, and stones (太半 of the total labor).
4. The remainder is the divisor.
5. Use the trench volume (in chi) as the dividend.
6. Divide the dividend by the divisor to get the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert to chi
下廣 = 1 * 10  # Convert to chi
深 = 6 + Fraction(3, 10)  # Convert to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert to chi

# Question 1: Calculate the volume of the trench
# Volume formula for a trapezoidal prism: V = ((top_width + bottom_width) / 2) * depth * length
積 = ((上廣 + 下廣) / 2) * 深 * 袤

# Convert the volume to chi and cun
積整數部分 = int(積)  # Whole chi
積小數部分 = (積 - 積整數部分) * 10  # Convert fractional chi to cun
積小數部分 = round(積小數部分, 1)  # Round to 1 decimal place (1 cun precision)

# Question 1 Answer
積結果 = f"{積整數部分} chi {積小數部分} cun"  # Volume in chi and cun

# Labor details
本人功 = 871  # Standard labor per person in chi
出土功 = Fraction(1, 5) * 本人功  # Earth removal labor
沙礫水石功 = Fraction(7, 10) * 本人功  # 太半 (more than half) of the labor
定功 = 232 + Fraction(4, 15)  # Adjusted labor in chi

# Procedure to calculate the number of workers
# Step 1: Subtract earth removal labor
剩餘功 = 本人功 - 出土功

# Step 2: Subtract sand, gravel, water, and stone labor
剩餘功 -= 沙礫水石功

# Step 3: Use the remainder as the divisor
法 = 剩餘功

# Step 4: Use the trench volume as the dividend
實 = 積

# Step 5: Divide to get the number of workers
a = Fraction(實, 法)

# Final answers
print(f"Trench volume: {積結果}")
print(f"Number of workers needed: {a} workers")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/174200"""
