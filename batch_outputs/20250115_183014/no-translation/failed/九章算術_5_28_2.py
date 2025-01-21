"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve this problem, we first calculate the volume of the irregular prism (冥谷) and then proceed to calculate the distance a person can transport and the number of workers required. Here's the step-by-step Python code:


"""


from fractions import Fraction

# 冥谷 dimensions
上廣 = 2 * 10  # Convert 丈 to 尺
袤上 = 7 * 10  # Convert 丈 to 尺
下廣 = 8       # Already in 尺
袤下 = 4 * 10  # Convert 丈 to 尺
深 = 6 * 10 + 5  # Convert 丈 and 尺 to 尺

# Calculate the average base area
上積 = 上廣 * 袤上
下積 = 下廣 * 袤下
平均積 = Fraction(上積 + 下積, 2)

# Calculate the total volume
積尺 = 平均積 * 深

# 車積尺 (volume a single cart can carry)
車積尺 = 201  # Given in the problem

# 往來步數 (round-trip distance in steps)
往來步數 = 1000  # 1 里 = 1000 步

# 車六人乘之 (6 people per cart)
車人數 = 6

# 法: 車積尺 * 往來步數
法 = 車積尺 * 往來步數

# Calculate the distance a person can transport
人到尺 = Fraction(法, 車人數)

# Calculate the number of workers required
用徒人數 = Fraction(積尺, 人到尺)

# Results
a = 人到尺  # Distance a person can transport
b = 用徒人數  # Number of workers required

# Outputs
print(f"人到 {a} 尺")
print(f"用徒 {b} 人")


"""


### Explanation of the Code:
1. **冥谷 Volume Calculation**:
   - The average base area is calculated using the formula `(上積 + 下積) / 2`.
   - The total volume is then calculated as `平均積 * 深`.

2. **Transportation Calculation**:
   - The volume a single cart can carry (`車積尺`) is multiplied by the round-trip distance (`往來步數`) to get the total work done by one cart in one trip.
   - Dividing this by the number of people per cart (`車人數`) gives the distance a single person can transport (`人到尺`).

3. **Worker Calculation**:
   - The total volume (`積尺`) is divided by the distance a person can transport (`人到尺`) to calculate the number of workers required (`用徒人數`).

### Final Outputs:
- `a` represents the distance a person can transport in 尺.
- `b` represents the number of workers required.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 33500
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 559/335"""
