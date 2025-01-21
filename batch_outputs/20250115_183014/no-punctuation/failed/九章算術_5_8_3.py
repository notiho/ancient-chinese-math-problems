"""
今有塹上廣一丈六尺三寸下廣一丈深六尺三寸袤一十三丈二尺一寸問積幾何
荅曰一萬九百四十三尺八寸
夏程人功八百七十一尺并出土功五分之一沙礫水石之功作太半定功二百三十二尺一十五分尺之四問用徒幾何
術曰置本人功去其出土功五分之一又去沙礫水石之功太半餘為法以塹積尺為實實如法而一即用徒人數
荅曰 a人 
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun
- Bottom width: 1 zhang
- Depth: 6 chi 3 cun
- Length: 13 zhang 2 chi 1 cun

Question 1: What is the volume of the trench in cubic chi?
Answer: 10,943 chi 8 cun.

Additionally:
- The standard work rate for a person is 871 cubic chi.
- The work for removing loose earth is 1/5 of the total.
- The work for sand, gravel, water, and stones is slightly more than half (太半, "greater half").
- The adjusted work rate is 232 chi and 4/15 chi.

Question 2: How many workers are required to complete the task?
Procedure: Take the standard work rate, subtract the work for removing loose earth (1/5), and subtract the work for sand, gravel, water, and stones (greater half). The remainder is the divisor.
Take the trench volume as the dividend. Divide the dividend by the divisor to find the number of workers.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the trench
上廣 = 1 * 10 + 6 + Fraction(3, 10)  # Convert zhang, chi, and cun to chi
下廣 = 1 * 10  # Convert zhang to chi
深 = 6 + Fraction(3, 10)  # Convert chi and cun to chi
袤 = 13 * 10 + 2 + Fraction(1, 10)  # Convert zhang, chi, and cun to chi

# Calculate the volume of the trench
# Volume = (Top Width + Bottom Width) * Depth * Length / 2
積 = (上廣 + 下廣) * 深 * 袤 / 2

# Convert the volume to chi and cun
積整數 = int(積)  # Whole chi
積小數 = 積 - 積整數  # Fractional part in chi
積寸 = 積小數 * 10  # Convert fractional chi to cun

# Output the volume
積結果 = f"{積整數} chi {積寸:.1f} cun"  # Format the result
print("Trench Volume:", 積結果)

# Standard work rate
本人功 = 871

# Work for removing loose earth (1/5 of the total)
出土功 = Fraction(1, 5) * 本人功

# Work for sand, gravel, water, and stones (greater half)
沙礫水石功 = Fraction(7, 12) * 本人功  # 太半 is interpreted as slightly more than 1/2

# Adjusted work rate
法 = 本人功 - 出土功 - 沙礫水石功

# Use the trench volume as the dividend
實 = 積

# Calculate the number of workers
a = Fraction(實, 法)

# Output the number of workers
print("Number of Workers:", a)
"""
Code error: unsupported format string passed to Fraction.__format__"""
