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
冥谷上廣 = Fraction(2)  # 上廣二丈 (2丈)
冥谷上袤 = Fraction(7)  # 上袤七丈 (7丈)
冥谷下廣 = Fraction(8, 10)  # 下廣八尺 (8尺 = 0.8丈)
冥谷下袤 = Fraction(4)  # 下袤四丈 (4丈)
冥谷深 = Fraction(6) + Fraction(5, 10)  # 深六丈五尺 (6丈5尺 = 6.5丈)

# Calculate the volume of the trapezoidal prism (積)
積 = (冥谷上廣 * 冥谷上袤 + 冥谷下廣 * 冥谷下袤) / 2 * 冥谷深
積_in_尺 = 積 * 10 * 10 * 10  # Convert from cubic 丈 to cubic 尺 (1丈 = 10尺)

# Given data for the second part
程行 = Fraction(58)  # 程行五十八里 (58里)
載土往來步數 = Fraction(200)  # 載土往來二百步 (200步)
載輸之間一里 = Fraction(1)  # 載輸之間一里 (1里)
車載 = Fraction(34) + Fraction(7, 10)  # 車載三十四尺七寸 (34尺7寸 = 34.7尺)
車人數 = Fraction(6)  # 六人共車 (6人)

# Calculate one person's contribution (人到尺)
程行步數 = 程行 * 360  # 1里 = 360步
總步數 = 載土往來步數 + 載輸之間一里 * 360
人到 = (車載 * 程行步數) / (總步數 * 車人數)

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
1. **Volume Calculation (積幾何)**:
   - The volume of the trapezoidal prism is calculated using the formula:
     \[
     \text{Volume} = \frac{(\text{上廣} \times \text{上袤} + \text{下廣} \times \text{下袤})}{2} \times \text{深}
     \]
   - Convert the result from cubic 丈 to cubic 尺 by multiplying by \(10^3\).

2. **Person's Contribution (人到尺)**:
   - The total steps for the journey are calculated as:
     \[
     \text{總步數} = \text{載土往來步數} + \text{載輸之間一里} \times 360
     \]
   - The total contribution of one person is:
     \[
     \text{人到} = \frac{\text{車載} \times \text{程行步數}}{\text{總步數} \times \text{車人數}}
     \]

3. **Number of Workers Needed (用徒)**:
   - The number of workers is calculated as:
     \[
     \text{用徒} = \frac{\text{積}}{\text{人到}}
     \]

### Final Results:
- `a`: The contribution of one person in cubic 尺.
- `b`: The number of workers needed.
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 30189/140
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 7826000/30189"""
