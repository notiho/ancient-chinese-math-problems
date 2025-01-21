"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
This problem involves calculating the volume of a valley and determining the distance each person can transport the soil and the number of workers required. Let's break it down step by step.

### Problem Setup
- The valley has an upper width of 2 zhang (20 chi), a length of 7 zhang (70 chi), a lower width of 8 chi, a length of 4 zhang (40 chi), and a depth of 6 zhang 5 chi (65 chi).
- The task is to calculate the volume of the valley and determine how far each person can transport the soil and how many workers are needed.

### Procedure
1. **Calculate the volume of the valley**:
   - The valley is a trapezoidal prism. The formula for the volume is:
     \[
     V = \frac{1}{2} \times (上廣 + 下廣) \times 深 \times 袤
     \]
   - Where:
     - 上廣 (upper width) = 20 chi
     - 下廣 (lower width) = 8 chi
     - 深 (depth) = 65 chi
     - 袤 (average length) = \((7 + 4) / 2 = 5.5\) zhang (55 chi)

2. **Calculate the distance each person can transport the soil**:
   - The formula is:
     \[
     人到 = \frac{\text{一車積尺} \times \text{程行步數}}{\text{今往來步數 + 載輸之間一里} \times \text{車六人}}
     \]
   - Where:
     - 一車積尺 (volume per cart) = 240 chi³
     - 程行步數 (distance per trip) = 300 bu (1 li = 300 bu)
     - 今往來步數 (round-trip steps) = 600 bu
     - 載輸之間一里 (loading/unloading distance) = 300 bu
     - 車六人 (6 people per cart)

3. **Calculate the number of workers required**:
   - The formula is:
     \[
     用徒 = \frac{\text{積尺}}{\text{人到}}
     \]

### Python Code


"""


from fractions import Fraction

# Dimensions of the valley
上廣 = 20  # chi
下廣 = 8   # chi
深 = 65    # chi
袤 = Fraction(7 + 4, 2) * 10  # Average length in chi (convert zhang to chi)

# Calculate the volume of the valley
積尺 = Fraction(1, 2) * (上廣 + 下廣) * 深 * 袤

# Parameters for transportation
一車積尺 = 240  # chi³
程行步數 = 300  # bu (1 li = 300 bu)
今往來步數 = 600  # bu
載輸之間一里 = 300  # bu
車六人 = 6  # people per cart

# Calculate the distance each person can transport the soil
法 = (今往來步數 + 載輸之間一里) * 車六人
實 = 一車積尺 * 程行步數
人到 = Fraction(實, 法)

# Calculate the number of workers required
用徒 = Fraction(積尺, 人到)

# Results
a = 人到  # Distance each person can transport the soil
b = 用徒  # Number of workers required

# Output results
a, b


"""


### Explanation of Results
- `a` represents the distance (in chi) each person can transport the soil.
- `b` represents the number of workers required to complete the task.

This code follows the procedure described in the problem and calculates the required values step by step.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 40/3
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 15015/4"""
