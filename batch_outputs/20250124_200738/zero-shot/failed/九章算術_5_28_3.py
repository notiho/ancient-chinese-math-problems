"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
載土往來二百步，載輸之間一里，程行五十八里，六人共車，車載三十四尺七寸。問︰人到積尺及用徒各幾何？
術曰：以一車積尺乘程行步數為實。置今往來步數，加載輸之間一里，以車六人乘之，為法。除之，所得即一人所到尺。以所到約積尺，即用徒人數。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
冥谷上廣 = Fraction(2)  # 二丈 (2丈)
冥谷上袤 = Fraction(7)  # 七丈 (7丈)
冥谷下廣 = Fraction(8, 10)  # 八尺 (8尺, converted to 丈: 1丈 = 10尺)
冥谷下袤 = Fraction(4)  # 四丈 (4丈)
冥谷深 = Fraction(6) + Fraction(5, 10)  # 六丈五尺 (6丈5尺, converted to 丈)

# Calculate the volume of the trapezoidal prism (積)
積 = (冥谷上廣 * 冥谷上袤 + 冥谷下廣 * 冥谷下袤) * 冥谷深 / 2
積_in_尺 = 積 * 10 * 10  # Convert from 丈³ to 尺³ (1丈 = 10尺)

# Given data for the second part
載土往來步數 = Fraction(200)  # 200步
載輸之間一里 = Fraction(360)  # 1里 = 360步
程行 = Fraction(58)  # 58里
車載 = Fraction(34) + Fraction(7, 10)  # 34尺7寸 (converted to 尺: 1尺 = 10寸)
車人數 = Fraction(6)  # 6人

# Calculate one person's contribution (人到尺)
總步數 = 載土往來步數 + 載輸之間一里
總積尺 = 車載 * 程行 * 360  # Convert 程行里 to steps (1里 = 360步)
人到 = 總積尺 / (總步數 * 車人數)

# Calculate the number of workers needed (用徒)
用徒 = 積_in_尺 / 人到

# Assign the results to variables
a = 人到
b = 用徒

# Results
a, b
#----- content ends here -----


"""


### Explanation:
1. **Volume Calculation**:
   - The volume of the trapezoidal prism is calculated using the formula for the volume of a trapezoidal prism:  
     \[
     V = \frac{1}{2} \times (上廣 \times 上袤 + 下廣 \times 下袤) \times 深
     \]
   - The result is converted from 丈³ to 尺³ by multiplying by \(10 \times 10\).

2. **One Person's Contribution**:
   - The total steps for one round trip are the sum of the round-trip steps and the steps for one-way transport.
   - The total volume transported is the product of the volume per cart, the total distance in steps, and the number of carts.

3. **Number of Workers Needed**:
   - The total volume is divided by the contribution of one person to determine the number of workers required.

### Final Output:
- `a`: The volume each person contributes (in 尺³).
- `b`: The number of workers needed.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 30189/140
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 782600/30189"""
