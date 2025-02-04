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

Additionally:
- The standard labor capacity is 871 chi.
- The effort for removing soil is reduced by 1/5.
- The effort for sand, gravel, water, and stone is increased by more than half (3/2).
- The adjusted labor capacity is 232 chi and 4/15 chi.

Question 2: How many workers are required?

The procedure says:
1. Place the standard labor capacity.
2. Subtract 1/5 for the effort of removing soil.
3. Subtract 3/2 for the effort of sand, gravel, water, and stone.
4. The remainder is the divisor.
5. Use the trench volume as the dividend.
6. Divide the dividend by the divisor to determine the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert to chi
下廣 = 1 * 10  # Convert to chi
深 = 6 + Fraction(3, 10)  # Convert to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert to chi

# Calculate the volume of the trench
# Volume formula for a trapezoidal prism: V = (1/2) * (top width + bottom width) * depth * length
積 = Fraction(1, 2) * (上廣 + 下廣) * 深 * 袤

# Convert the volume to chi and cun
積整數部分 = int(積)  # Whole chi
積小數部分 = 積 - 積整數部分  # Fractional part in chi
積寸 = 積小數部分 * 10  # Convert fractional chi to cun

# Standard labor capacity
本人功 = 871

# Adjustments to labor capacity
出土功減少 = Fraction(1, 5) * 本人功  # 1/5 reduction for removing soil
沙礫水石增加 = Fraction(3, 2) * 本人功  # 3/2 increase for sand, gravel, water, and stone
定功 = 本人功 - 出土功減少 - 沙礫水石增加  # Adjusted labor capacity

# Calculate the number of workers required
a = Fraction(積, 定功)

# Output results
積結果 = f"{積整數部分} chi {積寸} cun"
a結果 = f"{a} workers"

積結果, a結果#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: -3126807/174200"""
