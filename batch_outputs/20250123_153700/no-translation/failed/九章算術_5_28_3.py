"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To calculate the solution based on the given problem and procedure, let's break it down step by step:

### Step 1: Calculate the volume of the irregular prism (冥谷積)
The volume is calculated as the average of the top and bottom areas multiplied by the depth.



### Step 2: Calculate the distance one person can transport (人到)
The procedure specifies using a single cart's volume, the distance traveled, and the number of people per cart.



### Step 3: Calculate the number of people required (用徒)
The number of people required is based on the total volume divided by the distance one person can transport.



### Final Results

"""


from fractions import Fraction

# 上廣二丈，袤七丈
上廣 = 2 * 10  # Convert 丈 to 尺
上袤 = 7 * 10  # Convert 丈 to 尺
上積 = 上廣 * 上袤

# 下廣八尺，袤四丈
下廣 = 8  # Already in 尺
下袤 = 4 * 10  # Convert 丈 to 尺
下積 = 下廣 * 下袤

# 深六丈五尺
深 = 6 * 10 + 5  # Convert 丈 to 尺 and add the remaining 尺

# 冥谷積 = ((上積 + 下積) / 2) * 深
冥谷積 = Fraction((上積 + 下積), 2) * 深

# 一車積尺 (冥谷積)
一車積尺 = 冥谷積

# 程行步數 (往來步數 + 載輸之間一里)
往來步數 = 1000  # 一里 = 1000 步
程行步數 = 往來步數 * 2  # 往返

# 車六人乘之
車人數 = 6

# 法 = 程行步數 * 車人數
法 = 程行步數 * 車人數

# 人到 = 一車積尺 / 法
人到 = Fraction(一車積尺, 法)

# 用徒 = 冥谷積 / 人到
用徒 = Fraction(冥谷積, 人到)

a = 人到  # 人到 a尺
b = 用徒  # 用徒 b人


"""


This code calculates the distance one person can transport (`a`) and the number of people required (`b`) based on the given procedure.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 559/120
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 12000"""
