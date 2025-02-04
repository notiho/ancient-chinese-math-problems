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
- Top width: 1 zhang, 6 chi, 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi, 3 cun
- Length: 13 zhang, 2 chi, 1 cun

Question 1: What is the total volume of the trench?
Answer: 10,943 chi and 8 cun.

Additionally:
- The standard work rate for one person is 871 chi.
- The work for removing soil is 1/5 of the total work.
- The work for sand, gravel, water, and stones is slightly more than half (太半, "greater half").
- The final adjusted work rate is 232 chi and 4/15 chi.

Question 2: How many workers are needed to complete the task?

The procedure says:
1. Place the standard work rate per person.
2. Subtract the work for removing soil (1/5 of the total).
3. Subtract the work for sand, gravel, water, and stones (greater half of the total).
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

# Question 1: Calculate the volume of the trench
# Volume formula for a trapezoidal prism: V = (1/2) * (top width + bottom width) * depth * length
積 = Fraction(1, 2) * (上廣 + 下廣) * 深 * 袤

# Convert the volume to chi and cun
積整數部分 = int(積)  # Whole chi
積小數部分 = (積 - 積整數部分) * 10  # Convert fractional chi to cun
積小數部分 = round(積小數部分, 1)  # Round to 1 decimal place (precision for cun)

# Question 1 Answer
積答案 = f"{積整數部分} chi and {積小數部分} cun"

# Standard work rate per person
本人功 = 871

# Adjustments to the work rate
出土功 = Fraction(1, 5) * 本人功  # Work for removing soil
沙礫水石功 = Fraction(7, 12) * 本人功  # Greater half of the total (太半)

# Final adjusted work rate
法 = 本人功 - 出土功 - 沙礫水石功

# Use the trench volume as the dividend
實 = 積

# Calculate the number of workers
a = Fraction(實, 法)

# Question 2 Answer
a整數部分 = int(a)  # Whole number of workers
a小數部分 = (a - a整數部分)  # Fractional part of workers
a答案 = f"{a整數部分} workers and {a小數部分} fractional workers"

# Outputs
積答案, a答案#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 164157/3484, Actual: 65662947/1132300"""
