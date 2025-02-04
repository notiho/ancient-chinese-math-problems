"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰：一萬九百四十三尺八寸。
夏程人功八百七十一尺。并出土功五分之一，沙礫水石之功作太半，定功二百三十二尺、一十五分尺之四。問︰用徒幾何？
術曰：置本人功，去其出土功五分之一，又去沙礫水石之功太半，餘為法。以塹積尺為實。實如法而一，即用徒人數。
荅曰： a人 。
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
- A worker's capacity is 871 chi.
- Removing the earth requires 1/5 of the total effort.
- The effort for sand, gravel, water, and stones is more than half (3/5 of the total effort).
- The adjusted capacity is 232 chi and 4/15 chi.

Question 2: How many workers are needed?
The procedure says:
- Place the worker's capacity, subtract 1/5 for removing earth, and subtract 3/5 for sand, gravel, water, and stones. The remainder is the divisor.
- Use the trench's volume as the dividend.
- Divide the dividend by the divisor to determine the number of workers needed.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # 1丈6尺3寸
下廣 = 1 * 10  # 1丈
深 = 6 + Fraction(3, 10)  # 6尺3寸
袤 = 13 * 10 + 2 + Fraction(1, 10)  # 13丈2尺1寸

# Calculate the volume of the trench
# Volume formula for a trapezoidal prism: V = (1/2) * (top width + bottom width) * depth * length
積 = Fraction(1, 2) * (上廣 + 下廣) * 深 * 袤

# Convert the volume to chi and cun
積_尺 = int(積)  # Whole chi
積_寸 = (積 - 積_尺) * 10  # Remaining cun

# Display the volume
print(f"Trench volume: {積_尺} chi {積_寸} cun")

# Worker capacity
本人功 = 871

# Adjust worker capacity
# Remove 1/5 for removing earth
出土功 = Fraction(1, 5) * 本人功
# Remove 3/5 for sand, gravel, water, and stones
沙礫水石功 = Fraction(3, 5) * 本人功
# Remaining capacity
法 = 本人功 - 出土功 - 沙礫水石功

# Determine the number of workers needed
實 = 積
a = Fraction(實, 法)

# Display the number of workers
print(f"Number of workers needed: {a} workers")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 21887649/348400"""
