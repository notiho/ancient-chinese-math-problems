"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a valley and determining how far a person can transport the earth and how many workers are needed. Let's break it down step by step.

### Problem Breakdown:
1. **Volume Calculation**:
   - The valley has an upper width of 2 zhang, a length of 7 zhang, a lower width of 8 chi, a length of 4 zhang, and a depth of 6 zhang 5 chi.
   - The volume is calculated using the trapezoidal prism formula.

2. **Transport Calculation**:
   - Determine how far one person can transport the earth (in chi).
   - Calculate the number of workers required to transport the total volume.

---

### Solution in Python Code:


"""


from fractions import Fraction

# 冥谷 dimensions
上廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上袤 = 7 * 10  # Convert zhang to chi
下廣 = 8       # Already in chi
下袤 = 4 * 10  # Convert zhang to chi
深 = 6 * 10 + 5  # Convert depth to chi (6 zhang 5 chi)

# Calculate the average width and length
平均廣 = Fraction(上廣 + 下廣, 2)
平均袤 = Fraction(上袤 + 下袤, 2)

# Calculate the volume (積)
積 = 平均廣 * 平均袤 * 深

# Transport Calculation
# 車積尺 (volume per cart)
車積尺 = 200  # Assume 200 chi^3 per cart as a standard

# 程行步數 (distance in steps)
程行步數 = 300  # Assume 300 steps as a standard distance

# 今往來步數，加載輸之間一里 (round trip distance in steps)
往來步數 = 程行步數 * 2 + 1800  # 1 li = 1800 steps

# 車六人乘之 (6 people per cart)
法 = 車積尺 * 程行步數 * 6

# Calculate how far one person can transport (人到)
人到 = Fraction(車積尺 * 程行步數, 法)

# Calculate the number of workers needed (用徒)
用徒 = Fraction(積, 人到)

# Convert results to mixed fractions for clarity
a = 人到
b = 用徒

# Output results
a_mixed = (a.numerator // a.denominator, a.numerator % a.denominator, a.denominator)
b_mixed = (b.numerator // b.denominator, b.numerator % b.denominator, b.denominator)

print(f"人到: {a_mixed[0]}尺, {a_mixed[1]}/{a_mixed[2]}尺")
print(f"用徒: {b_mixed[0]}人, {b_mixed[1]}/{b_mixed[2]}人")


"""


---

### Explanation of the Code:
1. **Volume Calculation**:
   - The average width and length are calculated using the trapezoidal formula.
   - The total volume is then calculated by multiplying the average width, average length, and depth.

2. **Transport Calculation**:
   - The formula for how far one person can transport is derived from the problem's procedure.
   - The number of workers required is calculated by dividing the total volume by the distance one person can transport.

3. **Output**:
   - The results are converted into mixed fractions for clarity, as the problem involves fractional values.

---

### Final Answer:
- 人到: *a* chi (distance one person can transport).
- 用徒: *b* people (number of workers required).
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 1/6
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 300300"""
